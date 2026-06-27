{
    'name': 'Cockpit Antsoroko',
    'version': '1.0',
    'category': 'Cockpit',
    'summary': 'Module cockpit pour la gestion des produits Antsoroko',
    'depends': ['base', 'web', 'cockpit_erp_sedric'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_root.xml',
        'views/menu.xml',
        'views/antsoroko_brut_views.xml',
        'views/antsoroko_mc_views.xml',
        'views/antsoroko_extra_views.xml',
        'views/antsoroko_brise_views.xml',
        'views/antsoroko_dechet_views.xml',
        'views/antsoroko_karokany_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}

