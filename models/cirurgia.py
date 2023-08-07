from odoo import models, fields


class Cirurgia(models.Model):
    _name = 'cirurgia'
    _description = 'Cirurgia'

    conta = fields.Char(string='Conta')
    data_conta = fields.Date(string='Data da Conta')
    descricaoamb = fields.Char(string="Descrição")
    valor_original = fields.Float(string='Valor Original', digits=(10, 2))
    medico_id = fields.Many2one('usuarios', string='Médico')
    valor_medico = fields.Float(string='Valor Médico', digits=(10, 2))
    valor_glosa = fields.Float(string='Valor Glosa', digits=(10, 2))
    valor_imposto = fields.Float(string="Valor Imposto", digits=(10, 2))
    valor_administracao = fields.Float(string="Valor Taxa", digits=(10, 2))
    doctor_id = fields.Many2one('doctor', string='Fechamento', inverse_name='cirurgia_ids')