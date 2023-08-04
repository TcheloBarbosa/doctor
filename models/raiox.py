from odoo import models, fields


class Raiox(models.Model):
    _name = 'raiox'
    _description = 'Raiox Model'

    conta = fields.Char(string='Conta')
    data_conta = fields.Date(string='Data da Conta')
    valor_original = fields.Float(string='Valor Original')
    valor_clinica = fields.Float(string='Valor Clínica')
    valor_medico = fields.Float(string='Valor Médico')
    valor_glosa = fields.Float(string='Valor Glosa')
    doctor_id = fields.Many2one('doctor', string='Médico', inverse_name='raiox_ids')
