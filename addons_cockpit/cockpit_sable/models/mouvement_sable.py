from odoo import models, fields

class MouvementSable(models.Model):
    _name = "mouvement.sable"
    _description = "Mouvement de sable par camion"

    date = fields.Date(string="Date")
    heure_depart = fields.Datetime(string="Heure départ")
    heure_retour = fields.Datetime(string="Heure retour")
    libelle = fields.Char(string="Libellé")
    chauffeur = fields.Char(string="Chauffeur")
    vehicule = fields.Selection([
        ('dong_feng', 'Dong Feng'),
        ('t_king', 'T-King'),
        ('daf', 'DAF')
    ], string="Véhicule")
    nb_voyage = fields.Integer(string="Nb voyages")
    quantite = fields.Float(string="Quantité sable (m³)")
    prix_sable = fields.Float(string="Prix unitaire")
    recharge_gasoil = fields.Float(string="Recharge gasoil (L)")
    depense_libelle = fields.Char(string="Dépense libellé")
    depense_montant = fields.Float(string="Dépense montant")
    remarque = fields.Text(string="Remarque")

