document.addEventListener("DOMContentLoaded", function () {
    const enableCheckbox = document.querySelector("#id_enable_crazy_settings");
    const crazySettingsSection = document.querySelector("#crazy-settings-section");
    const body = document.body;

    if (enableCheckbox && crazySettingsSection) {
        // Функция для применения Crazy Settings
        function applyCrazySettings() {
            if (enableCheckbox.checked) {
                // Включаем Crazy Settings
                const fontSize = document.querySelector("#id_font_size").value || 14;
                const fontFamily = document.querySelector("#id_font_family").value || "Arial";
                const kerning = document.querySelector("#id_kerning").value || 1.0;
                const lineSpacing = document.querySelector("#id_line_spacing").value || 1.5;

                body.style.fontSize = `${fontSize}px`;
                body.style.fontFamily = fontFamily;
                body.style.letterSpacing = `${kerning}em`;
                body.style.lineHeight = lineSpacing;
            } else {
                // Отключаем Crazy Settings
                body.style.fontSize = "";
                body.style.fontFamily = "";
                body.style.letterSpacing = "";
                body.style.lineHeight = "";
            }
        }

        // При загрузке страницы применяем настройки
        crazySettingsSection.style.display = enableCheckbox.checked ? "block" : "none";
        applyCrazySettings();

        // Обработчик для чекбокса
        enableCheckbox.addEventListener("change", function () {
            crazySettingsSection.style.display = this.checked ? "block" : "none";
            applyCrazySettings();
        });

        // Обработчики для изменений значений Crazy Settings
        const crazyFields = document.querySelectorAll(
            "#id_font_size, #id_font_family, #id_kerning, #id_line_spacing"
        );
        crazyFields.forEach((field) => {
            field.addEventListener("input", applyCrazySettings);
        });
    }
});
