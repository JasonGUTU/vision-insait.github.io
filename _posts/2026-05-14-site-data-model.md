---
title: Site launch — data model for people, topics, and papers
date: 2026-05-14
categories: news
---

This site demonstrates how to wire **Jekyll collections** so that:

- Each `_people/*.md` entry defines `person_id` and `topics`.
- Each `_publications/*.md` entry lists `authors` as `person_id` values.
- Topic pages aggregate members automatically via Liquid.

Replace sample content with your group's real data.
