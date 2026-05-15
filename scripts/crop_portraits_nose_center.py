#!/usr/bin/env python3
"""Crop square portraits with the nose at the center of the output."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "assets" / "images" / "people"
BACKUP_DIR = PEOPLE_DIR / "_original"
YUNET_MODEL = ROOT / "assets" / "models" / "face_detection_yunet_2023mar.onnx"
OUTPUT_SIZE = 1024
# Face bbox width should be this fraction of the output square side.
FACE_WIDTH_FRAC = 1 / 3
MIN_HALF_SIZE = 80


def create_detector(input_size: tuple[int, int]) -> cv2.FaceDetectorYN:
    if not YUNET_MODEL.is_file():
        raise FileNotFoundError(f"Missing model: {YUNET_MODEL}")
    det = cv2.FaceDetectorYN.create(str(YUNET_MODEL), "", input_size)
    det.setScoreThreshold(0.6)
    det.setNMSThreshold(0.3)
    det.setTopK(5000)
    return det


def pick_largest_face(faces: np.ndarray) -> np.ndarray | None:
    if faces is None or len(faces) == 0:
        return None
    areas = faces[:, 2] * faces[:, 3]
    return faces[int(np.argmax(areas))]


def estimate_face_width(face: np.ndarray) -> float:
    """Estimate face width from YuNet bbox and eye distance."""
    bw = float(face[2])
    right_eye = np.array([face[4], face[5]], dtype=np.float64)
    left_eye = np.array([face[6], face[7]], dtype=np.float64)
    eye_dist = float(np.linalg.norm(right_eye - left_eye))
    if eye_dist > 1:
        return max(bw, eye_dist * 2.05)
    return bw


def nose_centered_crop_box(face: np.ndarray) -> tuple[int, int, int]:
    # YuNet: bbox + 5 landmarks (right eye, left eye, nose, mouth corners).
    nose = np.array([face[8], face[9]], dtype=np.float64)
    face_width = estimate_face_width(face)
    side = max(face_width / FACE_WIDTH_FRAC, MIN_HALF_SIZE * 2)
    half = side / 2

    x0 = int(round(nose[0] - half))
    y0 = int(round(nose[1] - half))
    return x0, y0, int(round(side))


def bbox_fallback_crop(face: np.ndarray) -> tuple[int, int, int]:
    x, y, bw, bh = face[:4]
    nose_x = x + bw * 0.5
    nose_y = y + bh * 0.42
    side = max(bw / FACE_WIDTH_FRAC, MIN_HALF_SIZE * 2)
    half = side / 2
    return int(round(nose_x - half)), int(round(nose_y - half)), int(round(side))


def pad_and_crop(bgr: np.ndarray, x0: int, y0: int, side: int) -> np.ndarray:
    h, w = bgr.shape[:2]
    x1, y1 = x0 + side, y0 + side
    pad_l = max(0, -x0)
    pad_t = max(0, -y0)
    pad_r = max(0, x1 - w)
    pad_b = max(0, y1 - h)
    if any((pad_l, pad_t, pad_r, pad_b)):
        bgr = cv2.copyMakeBorder(
            bgr, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_REPLICATE
        )
        x0 += pad_l
        y0 += pad_t
    return bgr[y0 : y0 + side, x0 : x0 + side]


def process_file(path: Path, detector: cv2.FaceDetectorYN) -> str:
    bgr = cv2.imread(str(path))
    if bgr is None:
        return "read_error"
    h, w = bgr.shape[:2]
    detector.setInputSize((w, h))
    _, faces = detector.detect(bgr)
    face = pick_largest_face(faces)
    if face is None:
        return "no_face"

    if face[14] < 0.5 or face[8] <= 0:
        box = bbox_fallback_crop(face)
    else:
        box = nose_centered_crop_box(face)

    cropped = pad_and_crop(bgr, *box)
    resized = cv2.resize(
        cropped, (OUTPUT_SIZE, OUTPUT_SIZE), interpolation=cv2.INTER_LANCZOS4
    )

    suffix = path.suffix.lower()
    if suffix == ".png":
        cv2.imwrite(str(path), resized, [cv2.IMWRITE_PNG_COMPRESSION, 3])
    else:
        cv2.imwrite(str(path), resized, [cv2.IMWRITE_JPEG_QUALITY, 92])
    return "ok"


def main() -> int:
    if not PEOPLE_DIR.is_dir():
        print(f"Missing {PEOPLE_DIR}", file=sys.stderr)
        return 1

    files = sorted(
        p
        for p in PEOPLE_DIR.iterdir()
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
        and not p.name.startswith(".")
    )
    if not files:
        print("No portrait files found.", file=sys.stderr)
        return 1

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    detector = create_detector((320, 320))
    ok: list[str] = []
    failed: list[tuple[str, str]] = []

    for path in files:
        backup = BACKUP_DIR / path.name
        if not backup.exists():
            shutil.copy2(path, backup)
        status = process_file(path, detector)
        if status == "ok":
            ok.append(path.name)
        else:
            failed.append((path.name, status))

    print(f"Processed: {len(ok)} / {len(files)}")
    print(
        f"Output: {OUTPUT_SIZE}x{OUTPUT_SIZE}, nose centered, "
        f"face width ~{int(FACE_WIDTH_FRAC * 100)}% of frame"
    )
    print(f"Backups: {BACKUP_DIR}")
    if failed:
        print("Failed:")
        for name, reason in failed:
            print(f"  - {name}: {reason}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
