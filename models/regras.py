from odoo import models, fields

class Regras(models.Model):
    _name = 'regras'
    usuario_prodoctor = fields.Many2many('usuarios', string='Usuário Prodoctor')
    consulta = fields.Float(string='Consulta')
    hon_medicos_percentual = fields.Boolean(string='Percentual Honorários Médicos')
    consulta_percentual = fields.Boolean(string='Percentual Consulta')
    honorarios_medicos = fields.Float(string='Honorários Médicos')
    honorarios_cirurgicos = fields.Float(string='Honorários Cirúrgicos')
    hon_cirurgicos_percentual = fields.Boolean(string='Percentual Honorários Cirúrgicos')
    imposto = fields.Float(string='Imposto')
    administracao = fields.Float(string='Administração')
    socio = fields.Boolean(string='Sócio')
    especifica_id = fields.Many2one('especificas', string='Regra Específica ID')
    