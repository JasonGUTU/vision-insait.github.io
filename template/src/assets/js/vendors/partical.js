(function () {
    const canvas = document.getElementById("starCanvas");
    const ctx = canvas.getContext("2d");

    function resizeCanvas() {
        const section = document.querySelector("section");
        canvas.width = section.clientWidth;
        canvas.height = section.clientHeight;
    }

    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    let stars = [];
    let numStars = 70;

    class Star {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.radius = Math.random() * 2;
            this.dy = Math.random() * 0.5 + 0.2;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = "white";
            ctx.fill();
        }
        update() {
            this.y += this.dy;
            if (this.y > canvas.height) {
                this.y = 0;
                this.x = Math.random() * canvas.width;
            }
            this.draw();
        }
    }

    function init() {
        stars = [];
        for (let i = 0; i < numStars; i++) {
            stars.push(new Star());
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        stars.forEach(star => star.update());
        requestAnimationFrame(animate);
    }

    init();
    animate();
})();
