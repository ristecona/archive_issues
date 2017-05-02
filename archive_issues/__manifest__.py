# -*- coding: utf-8 -*-

{
    'name': "Archive Issues",

    'summary': """
        Archive Multiple Issues using list view in odoo""",

    'description': """
        Archive Issues using list view in odoo
    """,
    'price': 69.99,
    'currency': 'EUR',


    'images': ['static/description/banner.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
