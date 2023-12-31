from odoo import models, fields


class Raiox(models.Model):
    _name = 'raiox'
    _description = 'Raiox Model'

    conta = fields.Char(string='Conta')
    data_conta = fields.Date(string='Data da Conta')
    valor_original = fields.Float(string='Valor Original', digits=(10, 2))
    valor_clinica = fields.Float(string='Valor Clínica', digits=(10, 2))
    medico_id = fields.Many2one('usuarios', string='Médico')
    valor_medico = fields.Float(string='Valor Médico', digits=(10, 2))
    valor_glosa = fields.Float(string='Valor Glosa', digits=(10, 2))
    valor_imposto = fields.Float(string= 'Valor Imposto', digits=(10, 2))
    doctor_id = fields.Many2one('doctor', string='Fechamento', inverse_name='raiox_ids')
