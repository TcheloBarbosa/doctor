from odoo import models, fields


class Consulta(models.Model):
    _name = 'consulta'
    _description = 'Consultas'

    conta = fields.Char(string='Conta')
    data_conta = fields.Date(string='Data da Conta')
    hora = fields.Datetime(string='Hora', time=True)
    valor_original = fields.Float(string='Valor Original', digits=(10, 2))
    medico_id = fields.Many2one('usuarios', string="Medico")
    valor_medico = fields.Float(string='Valor Médico', digits=(10, 2))
    valor_glosa = fields.Float(string='Valor Glosa', digits=(10, 2))
    valor_imposto = fields.Float(string="Valor Imposto", digits=(10, 2))
    valor_administracao = fields.Float(string="Valor Taxa", digits=(10, 2))
    valor_repasse = fields.Float(string="Valor Repasse", digits=(10, 2))
    usuario_repasse_id = fields.Many2one('usuarios', string="Usuário do Repasse")
    doctor_id = fields.Many2one('doctor', string='Fechamento', inverse_name='consulta_ids')
