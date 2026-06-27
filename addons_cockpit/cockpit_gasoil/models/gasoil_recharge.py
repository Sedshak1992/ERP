from odoo import models, fields, api

class GasoilRecharge(models.Model):
    _name = 'gasoil.recharge'
    _description = 'Recharge Gasoil par camion'

    date = fields.Date(string='Date')
    heure_depart = fields.Float(string='Heure Départ')
    heure_retour = fields.Float(string='Heure Retour')
    libelle = fields.Char(string='Libellé')
    chauffeur = fields.Char(string='Chauffeur')
    camion = fields.Selection([
        ('actros_1836', 'ACTROS (18 36)'),
        ('dongfeng', 'DONG FENG'),
        ('daf', 'DAF'),
        ('tking', 'T-KING'),
        ('jmc', 'JMC'),
        ('renauld_2540', 'RENAULD (25 40)'),
    ], string='Camion')
    quantite = fields.Float(string='Quantité (L)')
    cumul_quantite = fields.Float(string='Cumul Qté', compute='_compute_cumul_quantite', store=True)
    remarque = fields.Text(string='Remarque')

    name = fields.Char(string='Description', compute='_compute_name', store=True)

    @api.depends('quantite')
    def _compute_cumul_quantite(self):
        for record in self:
            record.cumul_quantite = record.quantite

    @api.depends('camion', 'date', 'quantite')
    def _compute_name(self):
        for rec in self:
            camion_label = dict(self._fields['camion'].selection).get(rec.camion, '')
            date_str = rec.date.strftime('%Y-%m-%d') if rec.date else ''
            rec.name = f"Recharge {camion_label} {date_str} {rec.quantite or 0}L"

