from odoo import models, fields

class Cirurgias(models.Model):
    _name = 'cirurgias'
    _description = 'Cirurgias'

    # Fields
    codigoamb = fields.Char(string='Nome')
    especialidade = fields.Many2one('especialidade', string="Especialidade")
    _rec_name = 'codigoamb'