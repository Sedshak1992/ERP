from odoo import models, fields, api

class AchatSable(models.Model):
    _name = 'achat.sable'
    _description = 'Achat de sable par camion'

    # Champs principaux
    date = fields.Date(string='Date')
    depart = fields.Char(string='Départ')   # texte libre
    retour = fields.Char(string='Retour')   # texte libre
    libelle = fields.Char(string='Libellé')
    chauffeur = fields.Char(string='Chauffeur')
    camion = fields.Selection([
        ('dongfeng', 'DONG FENG'),
        ('daf', 'DAF'),
        ('tking', 'T-KING'),
    ], string='Véhicule')

    nb_voyages = fields.Integer(string='Nombre de voyages')
    quantite = fields.Float(string='Quantité (m³)')
    cumul_quantite = fields.Float(string='Cumul Poids', compute='_compute_cumul_quantite', store=True)

    prix = fields.Float(string='Prix')   # prix fixe par voyage
    etat_paie = fields.Selection([
        ('paye', 'Payé'),
        ('non_paye', 'Non payé'),
    ], string='État')
    prix_total = fields.Float(string='Prix Total', compute='_compute_prix_total', store=True)

    # Carburant relié au module gasoil
    carburant_id = fields.Many2one('gasoil.mouvement', string='Recharge Gasoil')
    cumul_carburant = fields.Float(string='Cumul Recharge', compute='_compute_cumul_carburant', store=True)

    # Ristourne
    ristourne_bl = fields.Char(string='N° BL Ristourne')
    prix_ristourne = fields.Float(string='Prix Ristourne (FMG)')
    cumul_ristourne = fields.Float(string='Cumul Prix Ristourne', compute='_compute_cumul_ristourne', store=True)

    # Dépenses supplémentaires
    depense_libelle = fields.Char(string='Dépenses Supplémentaires')
    prix_depense = fields.Float(string='Prix Dépenses Supplémentaires')
    cumul_depense = fields.Float(string='Cumul Dépenses Supplémentaires', compute='_compute_cumul_depense', store=True)

    # Paiement
    total_paye = fields.Float(string='Total payé', compute='_compute_total_paye', store=True)
    cumul_paye = fields.Float(string='Cumul payé', compute='_compute_cumul_paye', store=True)

    remarque = fields.Text(string='Remarque')
    photo = fields.Binary(string='Photo du mouvement')

    # --- COMPUTES ---
    @api.depends('quantite')
    def _compute_cumul_quantite(self):
        total = sum(self.search([]).mapped('quantite'))
        for rec in self:
            rec.cumul_quantite = total

    @api.depends('prix', 'prix_depense', 'prix_ristourne')
    def _compute_total_paye(self):
        for rec in self:
            rec.total_paye = (rec.prix or 0) + (rec.prix_depense or 0) + (rec.prix_ristourne or 0)

    @api.depends('carburant_id')
    def _compute_cumul_carburant(self):
        total = sum(self.search([]).mapped('carburant_id.quantite'))
        for rec in self:
            rec.cumul_carburant = total

    @api.depends('prix_ristourne')
    def _compute_cumul_ristourne(self):
        total = sum(self.search([]).mapped('prix_ristourne'))
        for rec in self:
            rec.cumul_ristourne = total

    @api.depends('prix_depense')
    def _compute_cumul_depense(self):
        total = sum(self.search([]).mapped('prix_depense'))
        for rec in self:
            rec.cumul_depense = total

    @api.depends('total_paye')
    def _compute_cumul_paye(self):
        total = sum(self.search([]).mapped('total_paye'))
        for rec in self:
            rec.cumul_paye = total

