# Copyright (C) 2025 BlueBonnet
# Copyright 2026 Leonardo J. Caballero G.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Everee Base",
    "version": "18.0.1.0.0",
    "category": "Technical",
    "summary": "Base connector to integrate with Everee API",
    "author": "BlueBonnet, Leonardo J. Caballero G., Odoo Community Association (OCA)",
    "website": "https://github.com/macagua/",
    "maintainers": ["macagua"],
    "license": "AGPL-3",
    "depends": ["base", "base_setup"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "external_dependencies": {"python": ["requests"]},
    "installable": True,
    "application": False,
}
