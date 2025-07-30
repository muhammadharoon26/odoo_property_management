{
    "name": "Simple Property Management",
    "version": "1.8",
    "summary": "A simple model to manage real estate properties.",
    "description": """
        This module allows you to create and manage property records, including their type and status.
    """,
    "author": "Muhammad Haroon",
    "website": "http://www.yourcompany.com",
    "category": "Real Estate",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/property_view.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
