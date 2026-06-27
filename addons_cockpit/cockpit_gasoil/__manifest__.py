{
    'name': 'Cockpit GASOIL',
    'version': '1.0',
    'category': 'Cockpit',
    'summary': 'Module cockpit GASOIL : Entrée-Sortie + Recharge par Camion',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/gasoil_mouvement_views.xml',
        'views/gasoil_recharge_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}

