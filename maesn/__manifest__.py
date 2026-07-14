# -*- coding: utf-8 -*-
{
    "name": "maesn",
    "summary": "Connect Odoo to 50+ business tools with maesn Unified API",
    "description": """
maesn Unified API
=================
maesn lets SaaS companies connect Odoo to accounting, HR, ATS and project
management tools through a single unified API. This module adds a quick
access link to maesn from your Odoo menu.

Learn more at https://www.maesn.com
""",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "author": "maesn GmbH",
    "website": "https://www.maesn.com",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "data/menu.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
