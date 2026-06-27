{
    'name': 'Cockpit LOJY',
    'version': '1.0',
    'category': 'Cockpit',
    'summary': 'Module cockpit LOJY : Brut, HPS, Small, Brisé, Déchet, Karokany, Recap',
    'depends': ['base', 'web',
    'cockpit_erp_sedric',],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/lojy_brut_views.xml',
        'views/lojy_hps_views.xml',
        'views/lojy_small_views.xml',
        'views/lojy_brise_views.xml',
        'views/lojy_dechet_views.xml',
        'views/lojy_karokany_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}

