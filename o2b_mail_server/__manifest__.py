# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'O2b Mail Server',
    'version': '12.1',
    'category': 'Mail',
    'summary': 'O2b Mail Server Customisation',
    'description': """
Use Odoo mail server if define and after exceeding limit it uses Configured mail server.
    """,
    'depends': ['base','mail'],
    'data': [
        'ir_mail_server.xml',
    ],
    'installable': True,
    'auto_install': False,
}
