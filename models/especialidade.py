from odoo import models, fields

class Especialidade(models.Model):
    _name = 'especialidade'
    _description = 'Especialidade do profissional'

    # Fields
    nome = fields.Char(string='Nome')
    _rec_name = 'nome'