# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Intrastat Reporting',
    'version': '14.0.0.0.0',
    'category': 'Accounting',
    'description': """This module gives the details of the goods traded between the countries of European Union.""",
    'depends': ['base', 'product', 'delivery', 'stock', 'sale_management', 'purchase'],
    'data': [
        'data/report_intrastat_data.xml',
        'report/report_intrastat_invoice_template.xml',
        'report/report_intrastat_report.xml',
        'security/ir.model.access.csv',
        'security/report_intrastat_security.xml',
        'views/report_intrastat_views.xml',
    ],
}
