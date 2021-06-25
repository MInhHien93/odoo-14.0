{
    'name': "Pet+",
    'summary': """My pet plus""",
    'description': """My pet description""",
    'author': "Hien",
    'website': "https://minhng.info/odoo/thua-ke-model-trong-odoo.html",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'mypet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_plus_views.xml',
        'views/product_pet_views.xml',
    ],
    'installable': True,
    'application': True,
}