{
    'name': 'Sale Discount Golbal',
    'version': '0.1',
    'summary': 'Chiet khau tren toan bo hoa don ban.',
    'sequence': 90,
    'descripsion': """
    ##################
    """,
    'category': 'Sale',
    'depends': ['sale_stock'],
    'data': [
        'data/data.xml',
        'wizard/discount_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}