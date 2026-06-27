{
    'name': 'Cockpit ERP Sedric',
    'version': '16.0.1.0.0',
    'category': 'Cockpit',
    'summary': 'Module racine cockpit et Dashboard Boss',
    'description': 'Définit le menu principal Cockpit (menu_cockpit_root) et le tableau de bord boss.',
    'author': 'Sedric',
    'depends': [
        'base', 'web', 'mail',
        'cockpit_produits',
        'cockpit_sable',
        'cockpit_gasoil',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/menu.xml',
        'views/dashboard.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

