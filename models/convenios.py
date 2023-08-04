from odoo import models, fields

class Convenios(models.Model):
    _name = 'convenios'
    _description = 'Convênios'

    # Fields
    nome = fields.Char(string='Nome')
    codigo_prodoctor = fields.Integer(string="Código ProDoctor")
    _rec_name = 'nome'