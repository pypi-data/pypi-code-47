from django.conf import settings
from django.utils.translation import ugettext_lazy as _

MENUS = {
    "NAV_MENU_CORE": [
        {
            "name": _("Login"),
            "url": settings.LOGIN_URL,
            "icon": "lock_open",
            "validators": ["menu_generator.validators.is_anonymous"],
        },
        {
            "name": _("Account"),
            "url": "#",
            "icon": "person",
            "root": True,
            "validators": ["menu_generator.validators.is_authenticated"],
            "submenu": [
                {
                    "name": _("Stop impersonation"),
                    "url": "impersonate-stop",
                    "icon": "stop",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "aleksis.core.util.core_helpers.is_impersonate",
                    ],
                },
                {
                    "name": _("Logout"),
                    "url": "logout",
                    "icon": "exit_to_app",
                    "validators": ["menu_generator.validators.is_authenticated"],
                },
                {
                    "name": _("Two factor auth"),
                    "url": "two_factor:profile",
                    "icon": "phonelink_lock",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        lambda request: "two_factor" in settings.INSTALLED_APPS,
                    ],
                },
            ],
        },
        {
            "name": _("Admin"),
            "url": "#",
            "icon": "security",
            "validators": [
                "menu_generator.validators.is_authenticated",
                "menu_generator.validators.is_superuser",
            ],
            "submenu": [
                {
                    "name": _("Data management"),
                    "url": "data_management",
                    "icon": "view_list",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
                {
                    "name": _("System status"),
                    "url": "system_status",
                    "icon": "power_settings_new",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
                {
                    "name": _("Impersonation"),
                    "url": "impersonate-list",
                    "icon": "people",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
                {
                    "name": _("Manage school"),
                    "url": "school_management",
                    "icon": "school",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
                {
                    "name": _("Settings"),
                    "url": "site_settings",
                    "icon": "settings",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
            ],
        },
        {
            "name": _("People"),
            "url": "#",
            "root": True,
            "validators": [
                "menu_generator.validators.is_authenticated",
                "aleksis.core.util.core_helpers.has_person",
            ],
            "submenu": [
                {
                    "name": _("Persons"),
                    "url": "persons",
                    "validators": ["menu_generator.validators.is_authenticated"],
                },
                {
                    "name": _("Groups"),
                    "url": "groups",
                    "validators": ["menu_generator.validators.is_authenticated"],
                },
                {
                    "name": _("Persons and accounts"),
                    "url": "persons_accounts",
                    "validators": [
                        "menu_generator.validators.is_authenticated",
                        "menu_generator.validators.is_superuser",
                    ],
                },
            ],
        },
    ],
    "FOOTER_MENU_CORE": [
        {"name": _("Website"), "url": "https://aleksis.edugit.org/"},
        {"name": "Teckids e.V.", "url": "https://www.teckids.org/"},
    ],
    "DATA_MANAGEMENT_MENU": [],
    "SCHOOL_MANAGEMENT_MENU": [
        {"name": _("Edit school information"), "url": "edit_school_information", },
        {"name": _("Edit school term"), "url": "edit_school_term", },
    ],
}
