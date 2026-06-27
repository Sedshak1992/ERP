from odoo import models, fields, api

class BalanceSable(models.Model):
    _name = 'balance.sable'
    _description = 'Balance sable : synthèse achat/vente'

    date = fields.Date(string='Date')
    camion = fields.Char(string='Camion')
    client = fields.Char(string='Client')
    quantite_entree = fields.Float(string='Quantité entrée (achat)')
    quantite_sortie = fields.Float(string='Quantité sortie (vente)')
    stock_restant = fields.Float(string='Stock restant', compute='_compute_stock_restant', store=True)
    ecart = fields.Float(string='Écart', compute='_compute_ecart', store=True)
    remarque = fields.Text(string='Remarque')

    @api.depends('quantite_entree', 'quantite_sortie')
    def _compute_stock_restant(self):
        for record in self:
            record.stock_restant = record.quantite_entree - record.quantite_sortie

    @api.depends('stock_restant')
    def _compute_ecart(self):
        for record in self:
            record.ecart = record.stock_restant if record.stock_restant < 0 else 0.0

