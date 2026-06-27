from odoo import models, fields, api

class CockpitDashboard(models.Model):
    _name = 'cockpit.dashboard'
    _description = 'Cockpit Dashboard'

    name = fields.Char(string="Nom", required=True)

    # Relations vers tes modules métiers
    lojy_ids = fields.One2many('cockpit.lojy', 'dashboard_id', string="Lots Lojy")
    gasoil_ids = fields.One2many('cockpit.gasoil', 'dashboard_id', string="Mouvements Gasoil")
    sable_ids = fields.One2many('cockpit.sable', 'dashboard_id', string="Stocks Sable")
    antsoroko_ids = fields.One2many('cockpit.antsoroko', 'dashboard_id', string="Flux Antsoroko")
    produits_ids = fields.One2many('cockpit.produits', 'dashboard_id', string="Produits")

    # Champs calculés pour les indicateurs
    lojy_count = fields.Integer(string="Nb Lojy", compute="_compute_counts")
    gasoil_count = fields.Integer(string="Nb Gasoil", compute="_compute_counts")
    sable_count = fields.Integer(string="Nb Sable", compute="_compute_counts")
    antsoroko_count = fields.Integer(string="Nb Antsoroko", compute="_compute_counts")
    produits_count = fields.Integer(string="Nb Produits", compute="_compute_counts")

    @api.depends('lojy_ids','gasoil_ids','sable_ids','antsoroko_ids','produits_ids')
    def _compute_counts(self):
        for rec in self:
            rec.lojy_count = len(rec.lojy_ids)
            rec.gasoil_count = len(rec.gasoil_ids)
            rec.sable_count = len(rec.sable_ids)
            rec.antsoroko_count = len(rec.antsoroko_ids)
            rec.produits_count = len(rec.produits_ids)

