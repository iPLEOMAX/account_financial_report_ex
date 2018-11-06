# -*- coding: utf-8 -*-
{
    'name': "Account Financial Reports Extension",

    'summary': "Additional features for OCA Account Financial Reports",

    'description': """
        Additional features for OCA Account Financial Reports 
        that was developed by Odoo Community Association. 
        (Extension made for Al Salami Group, LLC.)""",

    'author': "Murshid C.",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Reporting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_financial_report'],

    # always loaded
    'data': [
        'views/general_ledger.xml',
    ],
}