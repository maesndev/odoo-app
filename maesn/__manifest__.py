# -*- coding: utf-8 -*-
{
    'name': 'maesn: Unified API for Accounting & ERP Integrations',
    'summary': 'Connect to Odoo & 50+ accounting solutions with one Unified API.',
    'description': """
maesn Unified API Connector
===========================

Connect your solution to Odoo and many other accounting systems through one API.

Key facts
---------

* One integration, 50+ supported systems: DATEV, SAP, Microsoft Dynamics, Sage,
  Visma, Exact Online and more
* Normalized data model for invoices, journal entries, contacts, payments,
  employees, projects and tasks
* Built and hosted in Germany, ISO 27001 certified, GDPR compliant and DORA-ready
* Trusted by leading SaaS companies, fintechs and banks

This module adds a maesn menu entry linking to
https://www.maesn.com/integrations/odoo where you can configure your integrations.
Using the maesn platform requires a maesn account (external service).
""",
    'version': '18.0.1.0.0',  # anpassen pro Odoo-Major-Version, z.B. 18.0.1.0.0
    'category': 'Technical',  # Alternative: 'Accounting' fuer bessere Sichtbarkeit
    'author': 'maesn GmbH',
    'website': 'https://www.maesn.com/integrations/odoo',
    'support': 'support@maesn.com',  # ggf. anpassen
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
    ],
    'images': [
        'static/description/Maesn_hero_16x9.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
