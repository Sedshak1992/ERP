from odoo import models, fields, api

class AntsorokoMC(models.Model):
    _name = 'antsoroko.mc'
    _description = 'Antsoroko MC - Sortie'

    date = fields.Date(string='Date')
    heure = fields.Float(string='Heure')
    vehicule = fields.Char(string='Véhicule')
    client = fields.Char(string='Client')
    type_mouvement = fields.Selection([
        ('sortie', 'Sortie')
    ], string='Type')
    nb_sacs = fields.Integer(string='Nb Sacs')
    cumul_sacs = fields.Integer(string='Cumul Sacs', compute='_compute_cumul_sacs', store=True)
    quantite = fields.Float(string='Quantité (Kg)')
    cumul_quantite = fields.Float(string='Cumul Qté', compute='_compute_cumul_qte', store=True)
    prix_kg = fields.Float(string='Prix/kg')
    montant_paye = fields.Float(string='Montant payé')
    cumul_montant = fields.Float(string='Cumul Montant', compute='_compute_cumul_montant', store=True)
    stock = fields.Float(string='Stock')
    remarque = fields.Text(string='Remarque')
    name = fields.Char(string='Description', compute='_compute_name', store=True)

    @api.depends('nb_sacs')
    def _compute_cumul_sacs(self):
        for rec in self:
            rec.cumul_sacs = rec.nb_sacs

    @api.depends('quantite')
    def _compute_cumul_qte(self):
        for rec in self:
            rec.cumul_quantite = rec.quantite

    @api.depends('montant_paye')
    def _compute_cumul_montant(self):
        for rec in self:
            rec.cumul_montant = rec.montant_paye

    @api.depends('date', 'vehicule', 'quantite')
    def _compute_name(self):
        for rec in self:
            date_str = rec.date.strftime('%Y-%m-%d') if rec.date else ''
            rec.name = f"MC {rec.vehicule or ''} {date_str} {rec.quantite or 0}Kg"

