// Theme Toggle Functionality
document.addEventListener("DOMContentLoaded", function () {
    const themeToggleBtn = document.getElementById("themeToggle");
    const themeIcon = themeToggleBtn.querySelector("i");

    // Check for saved theme preference or use device preference
    const savedTheme = localStorage.getItem("theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

    // Set initial theme based on saved preference or device preference
    if (savedTheme === "dark" || (!savedTheme && prefersDark)) {
        document.documentElement.setAttribute("data-theme", "dark");
        themeIcon.classList.remove("bx-moon");
        themeIcon.classList.add("bx-sun");
    }

    // Toggle theme on button click with micro-interactions
    themeToggleBtn.addEventListener("click", function() {
        // Add ripple effect
        const ripple = document.createElement('span');
        ripple.classList.add('theme-toggle-ripple');
        themeToggleBtn.appendChild(ripple);

        // Remove ripple after animation completes
        setTimeout(() => {
            ripple.remove();
        }, 600);

        const currentTheme = document.documentElement.getAttribute("data-theme") || "light";
        const newTheme = currentTheme === "light" ? "dark" : "light";

        // Apply theme with elegant transition
        document.body.classList.add("theme-transition");

        // Apply theme
        document.documentElement.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);

        // Update icon with animation
        if (newTheme === "dark") {
            themeIcon.classList.add('rotate-animation');
            setTimeout(() => {
                themeIcon.classList.remove("bx-moon");
                themeIcon.classList.add("bx-sun");
                themeIcon.classList.remove('rotate-animation');
            }, 150);
        } else {
            themeIcon.classList.add('rotate-animation');
            setTimeout(() => {
                themeIcon.classList.remove("bx-sun");
                themeIcon.classList.add("bx-moon");
                themeIcon.classList.remove('rotate-animation');
            }, 150);
        }

        // Remove transition class after animation completes
        setTimeout(() => {
            document.body.classList.remove("theme-transition");
        }, 1000);
    });
});