# -*- coding: utf-8 -*-
{
    'name': 'maesn: Unified API for Accounting, HR & ERP Integrations',
    'summary': 'Connect Odoo to DATEV, SAP, Sage, Visma and 50+ business tools '
               'through one Unified API.',
    'description': """
maesn Unified API Connector
===========================
Connect Odoo to accounting, HR, ATS and project management tools through one API.

Key facts
---------
* One integration, 50+ supported systems: DATEV, SAP, Microsoft Dynamics, Sage,
  Visma, Exact Online and more
* Normalized data model for invoices, journal entries, contacts, payments,
  employees, projects and tasks
* Built and hosted in Germany, GDPR compliant, DORA-ready
* Trusted by Tipalti, Rally (YC), Findity, Agicap and Nordhealth

This module adds a maesn menu entry linking to
https://www.maesn.com/integrations/odoo where you can configure integrations.
Using the maesn platform requires a maesn account (external service).
""",
    'version': '17.0.1.0.0',  # anpassen pro Odoo-Major-Version, z.B. 18.0.1.0.0
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
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
