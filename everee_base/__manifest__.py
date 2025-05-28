{
    "name": "Everee Base",
    "version": "18.0.1.0.0",
    "category": "Technical",
    "summary": "Base connector to integrate with Everee API",
    "author": "Bluebonnet",
    "website": "https://bluebonnet.io/",
    "maintainers": ["macagua"],
    "license": "Other proprietary",  # pylint: disable=license-allowed
    "depends": ["base", "base_setup"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "external_dependencies": {"python": ["requests"]},
    "installable": True,
    "application": False,
}
