from odoo import models, fields


class Usuarios(models.Model):
    _name = 'usuarios'
    _description = 'Usuários'

    # Fields
    nome = fields.Char(string='Nome')
    codigo_prodoctor = fields.Integer("Código ProDoctor")
    especialidade = fields.Many2one("especialidade", string='Especialidade')
    _rec_name = 'nome'
