{
    "name": "Human Resources Everee API Integration",
    "version": "18.0.1.0.0",
    "category": "Human Resources/Employees",
    "summary": "Human Resources Onboarding for the employees via Everee API",
    "author": "BlueBonnet",
    "website": "https://bluebonnet.io/",
    "maintainers": ["macagua"],
    "license": "Other proprietary",  # pylint: disable=license-allowed
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
