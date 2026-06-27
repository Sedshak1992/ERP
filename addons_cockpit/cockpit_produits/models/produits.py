from odoo import models, fields

class Produits(models.Model):
    _name = 'produits'
    _description = 'Produits divers'

    name = fields.Char(string="Nom du produit")
    categorie = fields.Selection([
        ('alimentaire', 'Alimentaire'),
        ('materiel', 'Matériel'),
        ('service', 'Service'),
    ], string="Catégorie")
    prix = fields.Float(string="Prix unitaire")
    unite = fields.Char(string="Unité de mesure")
    remarque = fields.Text(string="Remarque")

