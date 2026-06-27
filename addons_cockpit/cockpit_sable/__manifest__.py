{
    'name': 'Cockpit SABLE',
    'version': '1.0',
    'category': 'Cockpit',
    'summary': 'Module SABLE cockpit ERP',
    'depends': ['base', 'web', 'mail',],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/achat_sable_views.xml',
        'views/vente_sable_views.xml',
        'views/balance_sable_views.xml',
        'views/mouvement_sable_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}

