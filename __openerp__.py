# -*- coding: utf-8 -*-
{
    'name': "connecteur_seguinus",

    'summary': """
        This is intended to connect to the seguins program""",

    'description': """
        we'll see how we manage to do it.
    """,

    'author': "Simon Pessemesse",
    'website': "http://www.aubergedesseguins.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/connecteur_seguinus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}