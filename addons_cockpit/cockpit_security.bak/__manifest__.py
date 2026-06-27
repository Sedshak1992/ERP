{
    'name': 'Cockpit Security',
    'version': '16.0.1.0.0',
    'category': 'Cockpit',
    'summary': 'Gestion centralisée des rôles Cockpit (Opérateur, Superviseur)',
    'author': 'Sedric',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml'
    ],
    'installable': True,
    'application': True
}

