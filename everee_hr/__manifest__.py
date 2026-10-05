# Copyright (C) 2025 BlueBonnet
# Copyright 2026 Leonardo J. Caballero G.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Human Resources Everee API Integration",
    "version": "18.0.1.0.0",
    "category": "Human Resources/Employees",
    "summary": "Human Resources Onboarding for the employees via Everee API",
    "author": "BlueBonnet, Leonardo J. Caballero G., Odoo Community Association (OCA)",
    "website": "https://github.com/macagua/",
    "maintainers": ["macagua"],
    "license": "AGPL-3",
    "depends": ["hr", "everee_base"],
    "data": [
        "security/ir.model.access.csv",
        # "data/ir_actions_server_data.xml",
        "views/hr_employee_views.xml",
    ],
    "external_dependencies": {"python": ["requests"]},
    "installable": True,
    "application": False,
}
