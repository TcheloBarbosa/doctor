from odoo import models, fields


class Específicas(models.Model):
    _name = 'especificas'

    num_consulta_red = fields.Integer(string='Número Consulta Red')
    valor_percentual = fields.Float(string='Valor Percentual')
    repasse_direto = fields.Boolean(string='Repasse Direto')
    valor_percentual_rep = fields.Float(string='Valor Percentual Repasse')
    usuario_destino = fields.Many2one('usuarios', string='Usuário Destino Repasse')

    def name_get(self):
        result = []
        for record in self:
            name = f"Regra específica n. {record.id}"
            result.append((record.id, name))
        return result