
(() => {
    const STORAGE_KEY = "nexus-theme";
    const validThemes = ["system", "light", "dark"];

    function getPreference() {
        const saved = localStorage.getItem(STORAGE_KEY);
        return validThemes.includes(saved) ? saved : "system";
    }

    function getSystemTheme() {
        return window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark"
            : "light";
    }

    function applyTheme(preference) {
        const theme = preference === "system"
            ? getSystemTheme()
            : preference;

        document.documentElement.dataset.theme = theme;
        document.documentElement.dataset.bsTheme = theme;

        const button = document.getElementById("themeToggle");

        if (button) {
            const labels = {
                system: "Tema: Sistema",
                light: "Tema: Claro",
                dark: "Tema: Escuro"
            };

            button.textContent = labels[preference];
            button.setAttribute("aria-label", labels[preference]);
            button.title = "Alternar tema";
        }
    }

    function initializeTheme() {
        const preference = getPreference();

        applyTheme(preference);

        const button = document.getElementById("themeToggle");

        if (button) {
            button.addEventListener("click", () => {
                const themes = ["system", "light", "dark"];
                const current = getPreference();
                const next = themes[(themes.indexOf(current) + 1) % themes.length];

                localStorage.setItem(STORAGE_KEY, next);
                applyTheme(next);
            });
        }

        window.matchMedia("(prefers-color-scheme: dark)")
            .addEventListener("change", () => {
                if (getPreference() === "system") {
                    applyTheme("system");
                }
            });
    }

    document.addEventListener("DOMContentLoaded", initializeTheme);
})();
