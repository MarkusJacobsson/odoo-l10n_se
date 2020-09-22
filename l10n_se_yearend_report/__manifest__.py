# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2018 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sweden - Accounting Year End Reports',
    'version': '1.0',
    'category': 'Report',
    'description': """
Swedish accounting Year End Reports
===================================
http://www.srfredovisning.se/srf-mallar-for-arsredovisning-2/2-exempel/
http://www.srfredovisning.se/foretagsanalys-med-redovisningsinformation/3-analys-med-nyckeltal/
http://www.srfredovisning.se/foretagsanalys-med-redovisningsinformation/4-analys-med-kassafloden/

     """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['l10n_se_tax_report'],
    'data': [
        'wizard/year_end_report.xml',
    ],
    'demo_xml' : [],
    'installable': 'True',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
