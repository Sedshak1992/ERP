from odoo import models, fields
print(">>> cockpit_erp_sedric/cockpit_models.py chargé <<<")

class CockpitProduits(models.Model):
    _name = 'cockpit.produits'
    _description = 'Cockpit Produits'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom du produit", required=True, tracking=True)
    description = fields.Text(string="Description")
    dashboard_id = fields.Many2one('cockpit.dashboard', string="Dashboard")


class CockpitSable(models.Model):
    _name = 'cockpit.sable'
    _description = 'Cockpit Sable'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom du lot de sable", required=True, tracking=True)
    dashboard_id = fields.Many2one('cockpit.dashboard', string="Dashboard")


class CockpitGasoil(models.Model):
    _name = 'cockpit.gasoil'
    _description = 'Cockpit Gasoil'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom du lot de gasoil", required=True, tracking=True)
    dashboard_id = fields.Many2one('cockpit.dashboard', string="Dashboard")


class CockpitLojy(models.Model):
    _name = 'cockpit.lojy'
    _description = 'Cockpit Lojy'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom du lot LOJY", required=True, tracking=True)
    dashboard_id = fields.Many2one('cockpit.dashboard', string="Dashboard")


class CockpitAntsoroko(models.Model):
    _name = 'cockpit.antsoroko'
    _description = 'Cockpit Antsoroko'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nom du lot Antsoroko", required=True, tracking=True)
    dashboard_id = fields.Many2one('cockpit.dashboard', string="Dashboard")

