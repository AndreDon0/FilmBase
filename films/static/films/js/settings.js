document.addEventListener("DOMContentLoaded", function () {
    const enableCheckbox = document.querySelector("#id_enable_crazy_settings");
    const crazySettingsSection = document.querySelector("#crazy-settings-section");

    if (enableCheckbox && crazySettingsSection) {
        crazySettingsSection.style.display = enableCheckbox.checked ? "block" : "none";

        enableCheckbox.addEventListener("change", function () {
            crazySettingsSection.style.display = this.checked ? "block" : "none";
        });
    }
});
