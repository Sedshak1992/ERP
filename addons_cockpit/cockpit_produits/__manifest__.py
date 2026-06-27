{
    'name': 'Cockpit Produits',
    'version': '1.0',
    'category': 'Cockpit',
    'summary': 'Module cockpit pour rattachement des branches métier LOJY et ANTSOROKO',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

