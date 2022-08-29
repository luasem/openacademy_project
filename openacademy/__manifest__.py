{
    'name': "Open Academy",
    'summary': """
        The purpouse of this module is to work as an educative
        example of how to create one from scratch""",
    'author': "Jaime Alonso, Vauxoo",
    'website': "http://www.yourcompany.com",
    'license': 'LGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy_course_views.xml',
        'views/openacademy_menus.xml',
    ],
}
