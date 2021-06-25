{
    'name': 'Pet',
    'summary': '''My pet model''',
    'description': '''My pet description''',
    'author': 'Hien',
    'website': 'https://minhng.info/odoo/tao-model-trong-odoo.html',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
    ],
    'installable': True,
    'application': True,
}