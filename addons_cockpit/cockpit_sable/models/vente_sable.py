from odoo import models, fields, api

class VenteSable(models.Model):
    _name = 'vente.sable'
    _description = 'Vente de sable par camion'

    date = fields.Date(string='Date')
    heure_entree = fields.Float(string='Heure Entrée')
    heure_sortie = fields.Float(string='Heure Sortie')
    vehicule = fields.Char(string='Véhicule')
    client = fields.Char(string='Client')
    quantite = fields.Float(string='Quantité vendue (m3)')
    cumul_quantite = fields.Float(string='Cumul Quantité', compute='_compute_cumul_quantite', store=True)
    prix_unitaire = fields.Float(string='Prix unitaire')
    montant_paye = fields.Float(string='Montant payé')
    reste_a_payer = fields.Float(string='Reste à payer', compute='_compute_reste_a_payer', store=True)
    numero_bl = fields.Char(string='N° BL')
    quantite_restante = fields.Float(string='Quantité restante', compute='_compute_quantite_restante', store=True)
    remarque = fields.Text(string='Remarque')

    # Référence à la quantité achetée (à injecter dynamiquement ou manuellement)
    quantite_achat_reference = fields.Float(string='Quantité Achat Référence', default=0.0)

    @api.depends('quantite')
    def _compute_cumul_quantite(self):
        for record in self:
            record.cumul_quantite = record.quantite

    @api.depends('prix_unitaire', 'quantite', 'montant_paye')
    def _compute_reste_a_payer(self):
        for record in self:
            total = record.prix_unitaire * record.quantite
            record.reste_a_payer = total - record.montant_paye

    @api.depends('quantite_achat_reference', 'cumul_quantite')
    def _compute_quantite_restante(self):
        for record in self:
            record.quantite_restante = record.quantite_achat_reference - record.cumul_quantite

