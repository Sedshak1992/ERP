from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
_logger.info("✅ Modèle gasoil.mouvement chargé dans le registre")

class GasoilMouvement(models.Model):
    _name = 'gasoil.mouvement'
    _description = 'Entrée-Sortie Gasoil par camion'

    date = fields.Date(string='Date')

    # Heure saisie manuellement (ex: "14:30")
    heure = fields.Char(string="Heure (HH:MM)")

    type_mouvement = fields.Selection([
        ('entree','Entrée'),
        ('sortie','Sortie'),
    ], string='Type')

    camion = fields.Selection([
        ('dongfeng','DONG FENG'),
        ('daf','DAF'),
        ('tking','T-KING'),
        ('2624','26 24'),
        ('1836','18 36'),
        ('2540','25 40'),
    ], string='Camion')

    chauffeur = fields.Char(string='Chauffeur')

    # Nouveau champ Libellés
    libelle = fields.Char(string="Libellés")

    quantite = fields.Float(string='Quantité (L)')
    prix_unitaire = fields.Float(string='Prix unitaire')
    montant = fields.Float(string='Montant', compute='_compute_montant', store=True)
    remarque = fields.Text(string='Remarque')

    # Champ photo
    photo = fields.Binary(string="Photo du mouvement")

    name = fields.Char(string='Description', compute='_compute_name', store=True)

    stock_qty = fields.Float(string="Stock disponible", compute="_compute_stock_qty", store=True)

    @api.depends('quantite','prix_unitaire')
    def _compute_montant(self):
        for record in self:
            record.montant = record.quantite * record.prix_unitaire

    @api.depends('type_mouvement','camion','date','quantite','libelle')
    def _compute_name(self):
        for rec in self:
            type_label = dict(self._fields['type_mouvement'].selection).get(rec.type_mouvement, '')
            camion_label = dict(self._fields['camion'].selection).get(rec.camion, '')
            date_str = rec.date.strftime('%Y-%m-%d') if rec.date else ''
            rec.name = f"{type_label} {camion_label} {date_str} - {rec.quantite or 0}L ({rec.libelle or ''})"

    @api.depends('type_mouvement','quantite')
    def _compute_stock_qty(self):
        entree = sum(self.env['gasoil.mouvement'].search([('type_mouvement','=','entree')]).mapped('quantite'))
        sortie = sum(self.env['gasoil.mouvement'].search([('type_mouvement','=','sortie')]).mapped('quantite'))
        for rec in self:
            rec.stock_qty = entree - sortie

