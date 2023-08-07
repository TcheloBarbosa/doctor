from odoo import models, fields

class Procedimentos(models.Model):
    _name = 'procedimentos'
    _description = 'Procedimentos'

    # Fields
    codigoamb = fields.Char(string='Nome')
    especialidade_id = fields.Many2one('especialidade', string="Especialidade")
    _rec_name = 'codigoamb'