# hpm/i18n.py

LANGUAGES = {
    "en": {
        "description": "hpm: A simple and powerful package manager for Arch Linux.",
        "usage": "Usage",
        "dry_run_warning": "Running in dry-run mode. No changes will be made to the system.",
        "commands_title": "[bold blue]Available Commands[/bold blue]",
        "command_header": "Command",
        "description_header": "Description",
        "global_options_title": "Options",
        "dry_run_help": "Show what would be done without making any changes.",
        "lang_help": "Set the interface language.",
        "help_help": "Show this message and exit.",
        "command_aur_searching_helper": "Searching for AUR helper...",
        "command_aur_error_no_helper_found": "No AUR helper (yay or paru) found.",
        "command_aur_helper_install_info": "Please install an AUR helper to use this command.",
        "command_aur_using_helper": "Using AUR helper: {helper}",
        "command_aur_error_no_action_provided": "Please provide an action (e.g., install, remove, etc.).",
        "command_aur_installing_packages": "Installing AUR package(s): {packages}",
        "command_aur_removing_packages": "Removing AUR package(s): {packages}",
        "command_aur_searching_for_packages": "Searching for package(s): {packages}",
        "command_aur_upgrading_packages": "Upgrading packages...",
        "command_aur_error_unknown_action": "Error: Unknown action '{action}'.",
        "command_aur_error_no_package_provided": "Please provide a package name to install.",
        "command_aur_error_no_package_provided_remove": "Please provide a package name to remove.",
        "command_aur_error_no_search_term_provided": "Please provide a search term.",
        "dry_run_command_info": "The command that would be executed is: {command}",
        "operation_completed": "Operation completed successfully.",
        "command_aur_error_helper_not_found": "AUR helper not found. This error should not happen.",
        "command_aur_error_unexpected_error": "An unexpected error occurred: {error}",
        "commands": {
            "install": {"name": "install", "desc": "Installs one or more packages.", "aliases": ["i", "install"]},
            "remove": {"name": "remove", "desc": "Removes a package.", "aliases": ["r", "remove"]},
            "upgrade": {"name": "upgrade", "desc": "Upgrades all installed packages.", "aliases": ["u", "upgrade"]},
            "refresh": {"name": "refresh", "desc": "Synchronizes databases and upgrades packages.", "aliases": ["s", "refresh"]},
            "search": {"name": "search", "desc": "Searches for packages.", "aliases": ["q", "search"]},
            "info": {"name": "info", "desc": "Displays detailed package info.", "aliases": ["I", "info"]},
            "list": {"name": "list", "desc": "Lists all installed packages.", "aliases": ["l", "list"]},
            "clean": {"name": "clean", "desc": "Cleans the package cache.", "aliases": ["c", "clean"]},
            "orphans": {"name": "orphans", "desc": "Manages orphan packages.", "aliases": ["o", "orphans"]},
            "aur": {"name": "aur", "desc": "Manages packages from the AUR.", "aliases": ["a", "aur"]},
            "doctor": {"name": "doctor", "desc": "Performs a system health check.", "aliases": ["d", "doctor"]},
            "history": {"name": "history", "desc": "Displays command history.", "aliases": ["h", "history"]}
        }
    },
    "ar": {
        "description": "hpm: مدير حزم بسيط وقوي لـ Arch Linux.",
        "usage": "الاستخدام",
        "dry_run_warning": "يعمل في وضع التجربة. لن يتم إجراء أي تغييرات على النظام.",
        "commands_title": "[bold blue]الأوامر المتاحة[/bold blue]",
        "command_header": "الأمر",
        "description_header": "الوصف",
        "global_options_title": "الخيارات",
        "dry_run_help": "يعرض ما سيتم تنفيذه دون إجراء أي تغييرات.",
        "lang_help": "يضبط لغة الواجهة.",
        "help_help": "يعرض هذه الرسالة ويخرج.",
        "command_aur_searching_helper": "جارٍ البحث عن مساعد AUR...",
        "command_aur_error_no_helper_found": "لم يتم العثور على مساعد AUR (yay أو paru).",
        "command_aur_helper_install_info": "يرجى تثبيت مساعد AUR لاستخدام هذا الأمر.",
        "command_aur_using_helper": "يتم استخدام مساعد AUR: {helper}",
        "command_aur_error_no_action_provided": "يرجى تقديم إجراء (مثل تثبيت، إزالة، إلخ).",
        "command_aur_installing_packages": "جارٍ تثبيت حزمة(حزم) AUR: {packages}",
        "command_aur_removing_packages": "جارٍ إزالة حزمة(حزم) AUR: {packages}",
        "command_aur_searching_for_packages": "جارٍ البحث عن حزمة(حزم): {packages}",
        "command_aur_upgrading_packages": "جارٍ ترقية الحزم...",
        "command_aur_error_unknown_action": "خطأ: إجراء غير معروف '{action}'.",
        "command_aur_error_no_package_provided": "يرجى تقديم اسم حزمة للتثبيت.",
        "command_aur_error_no_package_provided_remove": "يرجى تقديم اسم حزمة للإزالة.",
        "command_aur_error_no_search_term_provided": "يرجى تقديم مصطلح للبحث.",
        "dry_run_command_info": "الأمر الذي سيتم تنفيذه: {command}",
        "operation_completed": "اكتملت العملية بنجاح.",
        "command_aur_error_helper_not_found": "لم يتم العثور على مساعد AUR. يجب ألا يحدث هذا الخطأ.",
        "command_aur_error_unexpected_error": "حدث خطأ غير متوقع: {error}",
        "commands": {
            "install": {"name": "تثبيت", "desc": "يثبت حزمة واحدة أو أكثر.", "aliases": ["i", "تثبيت", "install"]},
            "remove": {"name": "إزالة", "desc": "يزيل حزمة.", "aliases": ["r", "إزالة", "remove"]},
            "upgrade": {"name": "ترقية", "desc": "يرقي جميع الحزم المثبتة.", "aliases": ["u", "ترقية", "upgrade"]},
            "refresh": {"name": "تحديث", "desc": "يزامن قواعد البيانات ويرقي الحزم.", "aliases": ["s", "تحديث", "refresh"]},
            "search": {"name": "بحث", "desc": "يبحث عن حزم.", "aliases": ["q", "بحث", "search"]},
            "info": {"name": "معلومات", "desc": "يعرض معلومات مفصلة عن الحزمة.", "aliases": ["I", "معلومات", "info"]},
            "list": {"name": "قائمة", "desc": "يسرد جميع الحزم المثبتة.", "aliases": ["l", "قائمة", "list"]},
            "clean": {"name": "تنظيف", "desc": "ينظف ذاكرة التخزين المؤقت للحزم.", "aliases": ["c", "تنظيف", "clean"]},
            "orphans": {"name": "يتيم", "desc": "يدير الحزم اليتيمة.", "aliases": ["o", "يتيم", "orphans"]},
            "aur": {"name": "aur", "desc": "يدير حزم من Arch User Repository (AUR).", "aliases": ["a", "aur"]},
            "doctor": {"name": "فحص", "desc": "يقوم بفحص كامل لصحة النظام.", "aliases": ["d", "فحص", "doctor"]},
            "history": {"name": "سجل", "desc": "يعرض سجل الأوامر.", "aliases": ["h", "سجل", "history"]}
        }
    }
}

def get_translation(lang: str):
    """Retrieves a translation getter function for a given language."""
    if lang not in LANGUAGES:
        lang = "en"
    
    translations = LANGUAGES[lang]
    def translate(key: str):
        if key in translations:
            return translations[key]
        return LANGUAGES["en"][key]
    
    return translate

def get_full_translation_dict(lang: str):
    """Retrieves the full translation dictionary for a given language."""
    return LANGUAGES.get(lang, LANGUAGES["en"])
