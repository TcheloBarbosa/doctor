from odoo import models, fields
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


class Doctor(models.Model):
    _name = 'doctor'
    data_comeco = fields.Date("Data de Início")
    data_fim = fields.Date("Data do Fim")
    convenio_id = fields.Many2one('convenios', string='Convênio')
    medico_id = fields.Many2one('usuarios', string='Profisisonal')
    raiox_ids = fields.One2many('raiox', 'doctor_id', string='Raiox', readonly=True)
    pacientes_contas_procedimentos_ids = fields.One2many(
        'pacientes.contas.procedimentos',
        'doctor_id',
        string="Contas",
        readonly=True,
    )
    def name_get(self):
        result = []
        for record in self:
            name = f"Fechamento n. {record.id}"
            result.append((record.id, name))
        return result

    def compute_pacientes_contas_procedimentos(self):
        if self.data_comeco and self.data_fim:
            for doctor in self:
                external_data = self.env['pacientes.contas.procedimentos'].get_external_data(self.data_comeco, self.data_fim, self.medico_id.codigo_prodoctor, self.convenio_id.codigo_prodoctor)
                doctor.pacientes_contas_procedimentos_ids = [(0, 0, data) for data in external_data]
                #CÁLCULO DO RAIO-X
                if doctor.medico_id:
                    filtered_records = doctor.pacientes_contas_procedimentos_ids.search([('codigoamb', 'like', '4.08%')])
                    #mapped_records = filtered_records.mapped('conta')
                    regra = self.env['regras'].search([('usuario_prodoctor', '=', self.medico_id.id)], limit=1)
                    lista_vals = []
                    for rec in filtered_records:
                        vals_list = {
                            'conta': rec.conta,
                            'data_conta': rec.data,
                            'valor_original': rec.valortotal,
                            'valor_clinica': 0 if regra.socio else rec.valortotal,
                            'valor_medico': rec.valortotal if regra.socio else 0,
                            'valor_glosa': rec.valorglosa,
                            'doctor_id': self.id,
                        }
                        lista_vals.append(vals_list)
                    self.raiox_ids = self.env['raiox'].create(lista_vals)





