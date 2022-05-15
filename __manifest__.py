# -*- coding: utf-8 -*-
{
    'name': "My Hotel",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Huy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'sale_stock', 'account', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/hotel_customer_sequence.xml',
        'data/room_stage_data.xml',
        'data/hotel_sequence.xml',
        'views/data.xml',
        'views/room_view.xml',
        'views/service_views.xml',
        'views/roomtype_views.xml',
        'views/service_type_views.xml',
        'views/customer_view.xml',
        'views/employee_view.xml',
        'views/booking_view.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
