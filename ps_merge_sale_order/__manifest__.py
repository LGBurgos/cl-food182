# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) PySquad Informetics (<https://www.pysquad.com/>).
#
#    For Module Support : contact@pysquad.com
#
##############################################################################

{
    'name': 'Merge Sale Order',
    'version': '18.0',
    'category': 'Sales',
    'summary': 'Odoo module for customizable merging of sales orders',
    'description': """
            This module allows users to merge sales orders with different merge types, providing flexibility
            in handling sales orders based on specific requirements and workflows.
            """,

    'license': 'AGPL-3',
    'author': 'Pysquad Informatics LLP',
    'website': 'https://www.pysquad.com',
    'depends': ['base', 'sale_management'],
    'data': [
        "security/ir.model.access.csv",
        "views/inherit_sale_order_view.xml",
        "wizard/ps_merge_sale_order_view.xml",
    ],
    'images': [
        'static/description/merge_so_banner.png',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}