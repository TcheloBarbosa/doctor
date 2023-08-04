from odoo import models, fields

class Pacientes(models.Model):
    _name = 'pacientes'
    _description = 'Pacientes'

    # Fields
    nome = fields.Char(string='Nome')
    codigo_prodoctor = fields.Integer(string="Código ProDoctor")
    _rec_name = 'nome'
