from odoo import models, fields
from datetime import datetime, timedelta


class Doctor(models.Model):
    _name = 'doctor'
    data_comeco = fields.Date("Data de Início")
    data_fim = fields.Date("Data do Fim")
    convenio_id = fields.Many2one('convenios', string='Convênio')
    medico_id = fields.Many2one('usuarios', string='Profisisonal')
    raiox_ids = fields.One2many('raiox', 'doctor_id', string='Raiox', readonly=True)
    procedimento_ids = fields.One2many('procedimento', 'doctor_id', string="Procedimentos", readonly=True)
    consulta_ids = fields.One2many('consulta', 'doctor_id', string="Consultas", readonly=True)
    cirurgia_ids = fields.One2many('cirurgia', 'doctor_id', string="Cirurgia", readonly=True)
    pacientes_contas_procedimentos_ids = fields.One2many(
        'pacientes.contas.procedimentos',
        'doctor_id',
        string="Contas",
        readonly=True,
    )
    oculta_tree = fields.Boolean('Oculta tree', default=True)

    def relatorio_doctor(self):
        return {
            'type': 'ir.actions.report',
            'report_type': 'qweb-pdf',
            'report_name': 'doctor.relatorio_doctor',
            'context': {'model': 'doctor', 'active_id': self.id},
        }

    def mostrar_tudo(self):
        self.oculta_tree = not self.oculta_tree

    def name_get(self):
        result = []
        for record in self:
            name = f"Fechamento n. {record.id}"
            result.append((record.id, name))
        return result

    def valida_valor_cir(self, regra, valor):
        if regra.hon_cirurgicos_percentual:
            if regra.imposto != 0:
                return (valor * regra.honorarios_cirurgicos) / 100 - (valor * (regra.imposto / 100))
            else:
                return (valor * regra.honorarios_cirurgicos) / 100 - (valor * (regra.administracao / 100))
        else:
            if regra.imposto != 0:
                return regra.honoraios_cirurgicos - (valor * (regra.imposto) / 100)
            else:
                return regra.honoraios_cirurgicos - (valor * (regra.administracao) / 100)

    def valida_valor_procedimentos(self, regra, valor):
        if regra.hon_medicos_percentual:
            if regra.imposto != 0:
                return (valor - (valor * (regra.imposto) / 100)) * (regra.honorarios_medicos / 100)
            else:
                return (valor - (valor * (regra.administracao) / 100)) * (regra.honorarios_medicos / 100)
        else:
            if regra.imposto != 0:
                return regra.honorarios_medicos - (valor * (regra.imposto) / 100)
            else:
                return regra.honorarios_medicos - (valor * (regra.administracao) / 100)

    ###################################
    def valida_hora(self, lista_consultas, regra):
        lista_hr = []
        for dia in lista_consultas.mapped('data_conta'):
            contador = 0
            lista_hr = lista_consultas.filtered(lambda r: r.data_conta == dia).sorted(key=lambda r: r.hora)
            if len(lista_hr) < int(regra.especifica_id.num_consulta_red) or int(regra.especifica_id.num_consulta_red) == 0:
                if regra.consulta_percentual:
                    for consulta in lista_hr:
                        if regra.especifica_id.repasse_direto:
                            consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                            consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
                else:
                    for consulta in lista_hr:
                        consulta.valor_medico = regra.consulta - (
                                    regra.imposto / 100) if regra.imposto != 0 else regra.consulta - (
                                    regra.administracao / 100)
                        if regra.especifica_id.repasse_direto:
                            consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                            consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
            else:
                hora_limite = lista_hr[0].hora + timedelta(hours=1)
                for consulta in lista_hr:
                    if contador < int(regra.especifica_id.num_consulta_red):
                        if consulta.hora <= hora_limite:
                            if regra.cosulta_percentual:
                                if regra.especifica_id.repasse_direto:
                                    consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                                    consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
                            else:
                                consulta.valor_medico = regra.consulta - (
                                        regra.imposto / 100) if regra.imposto != 0 else regra.consulta - (
                                        regra.administracao / 100)
                                if regra.especifica_id.repasse_direto:
                                    consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                                    consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
                        else:
                            contador = 0
                            if regra.cosulta_percentual:
                                if regra.especifica_id.repasse_direto:
                                    consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                                    consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
                            else:
                                consulta.valor_medico = regra.consulta - (
                                        regra.imposto / 100) if regra.imposto != 0 else regra.consulta - (
                                        regra.administracao / 100)
                                if regra.especifica_id.repasse_direto:
                                    consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
                                    consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
            # consulta.valor_medico = consulta.valor_medico * regra.especifica_id.valor_percentual/100
            # if regra.especifica_id.repasse_direto:
            #     consulta.valor_repasse = consulta.valor_medico * regra.especifica_id.valor_percentual_rep / 100
            #     consulta.usuario_repasse_id = regra.especifica_id.usuario_destino
        return lista_hr

    def valida_consulta(self, regra, valor):
        if regra.consulta_percentual:
            if regra.consulta == 100:
                if regra.imposto != 0:
                    return (valor - (valor * (regra.imposto) / 100))
                else:
                    return (valor - (valor * (regra.administracao) / 100))
            else:
                if regra.imposto != 0:
                    return (valor - (valor * (regra.imposto) / 100) * regra.consulta / 100)
                else:
                    return (valor - (valor * (regra.administracao) / 100) * regra.consulta / 100)
        else:
            if regra.imposto != 0:
                return (valor - (valor * (regra.imposto) / 100))
            else:
                return (valor - (valor * (regra.administracao) / 100))

    def compute_pacientes_contas_procedimentos(self):
        if self.data_comeco and self.data_fim:
            for doctor in self:
                external_data = self.env['pacientes.contas.procedimentos'].get_external_data(self.data_comeco,
                                                                                             self.data_fim,
                                                                                             self.medico_id.codigo_prodoctor,
                                                                                             self.convenio_id.codigo_prodoctor)
                doctor.pacientes_contas_procedimentos_ids = [(0, 0, data) for data in external_data]
                # CÁLCULO DO RAIO-X
                if doctor.medico_id:
                    # filtered_records = doctor.pacientes_contas_procedimentos_ids.search([('codigoamb', 'like', '4.08%')])
                    # mapped_records = doctor.pacientes_contas_procedimentos_ids - filtered_records
                    regra = self.env['regras'].search([('usuario_prodoctor', '=', self.medico_id.id)], limit=1)
                    lista_vals = []
                    for rec in doctor.pacientes_contas_procedimentos_ids.filtered(
                            lambda r: r.codigoamb.startswith('4.08')):
                        vals_list = {
                            'conta': rec.conta,
                            'data_conta': rec.data,
                            'valor_original': rec.valortotal,
                            'valor_clinica': 0 if regra.socio else int(rec.valortotal) - 0.16,
                            'medico_id': self.medico_id.id,
                            'valor_medico': int(rec.valortotal) - 0.16 if regra.socio else 0,
                            'valor_glosa': rec.valorglosa,
                            'valor_imposto': int(rec.valortotal) * 0.16,
                            'doctor_id': self.id,
                        }
                        lista_vals.append(vals_list)
                    self.raiox_ids = self.env['raiox'].create(lista_vals)
                    lista_cirurgia = self.env['cirurgias'].search(
                        [('especialidade_id', '=', doctor.medico_id.especialidade_id.id)])
                    lilsta_reduzida = doctor.pacientes_contas_procedimentos_ids.filtered(
                        lambda r: r.codigoamb in lista_cirurgia.mapped('codigoamb'))
                    list_cir = []
                    for rec1 in lilsta_reduzida:
                        valor = self.valida_valor_cir(regra, rec1.valortotal)
                        vals_list_cir = {
                            'conta': rec1.conta,
                            'data_conta': rec1.data,
                            'descricaoamb': rec1.descricaoamb,
                            'valor_original': rec1.valortotal,
                            'medico_id': self.medico_id.id,
                            'valor_medico': valor,
                            'valor_glosa': rec1.valorglosa,
                            'valor_imposto': rec1.valortotal * (regra.imposto / 100) if regra.imposto != 0 else 0,
                            'valor_administracao': rec1.valortotal * (
                                    regra.administracao / 100) if regra.administracao != 0 else 0,
                            'doctor_id': rec1.doctor_id.id,  # Acessar o ID do registro relacionado
                        }
                        list_cir.append(vals_list_cir)
                    self.cirurgia_ids = self.env['cirurgia'].create(list_cir)
                    lista_proc = self.env['procedimentos'].search(
                        [('especialidade_id', '=', doctor.medico_id.especialidade_id.id)])
                    procedimentos = []
                    lista_procedimentos = doctor.pacientes_contas_procedimentos_ids.filtered(
                        lambda r: not r.codigoamb.startswith('4.08') and r.codigoamb in lista_proc.mapped(
                            'codigoamb')) - lilsta_reduzida
                    for rec2 in lista_procedimentos:
                        valor_proc = self.valida_valor_procedimentos(regra, rec2.valortotal)
                        vals_list_proc = {
                            'conta': rec2.conta,
                            'data_conta': rec2.data,
                            'descricaoamb': rec2.descricaoamb,
                            'valor_original': rec2.valortotal,
                            'medico_id': self.medico_id.id,
                            'valor_medico': valor_proc,
                            'valor_glosa': rec2.valorglosa,
                            'valor_imposto': rec2.valortotal * (regra.imposto / 100) if regra.imposto != 0 else 0,
                            'valor_administracao': rec2.valortotal * (
                                    regra.administracao / 100) if regra.administracao != 0 else 0,
                            'valor_repasse': 0 if not regra.especifica_id.repasse_direto else rec2.valortotal - (
                                rec2.valortotal * (regra.imposto / 100) if regra.imposto != 0 else rec2.valortotal * (
                                        regra.administracao / 100)) * (regra.especifica_id.valor_percentual_rep / 100),
                            'usuario_repasse_id': False if not regra.especifica_id.repasse_direto else regra.especifica_id.usuario_destino.id,
                            'doctor_id': rec2.doctor_id.id,  # Acessar o ID do registro relacionado
                        }
                        procedimentos.append(vals_list_proc)
                    self.procedimento_ids = self.env['procedimento'].create(procedimentos)
                    list_con = []
                    lista_consultas = doctor.pacientes_contas_procedimentos_ids.filtered(
                        lambda r: not r.codigoamb.startswith('4.08')) - lilsta_reduzida - lista_procedimentos
                    for rec3 in lista_consultas:
                        valor_con = self.valida_consulta(regra, rec3.valortotal)
                        vals_list_consulta = {
                            'conta': rec3.conta,
                            'data_conta': rec3.data,
                            'hora': datetime.strptime(rec3.horainicial, "%H:%M"),
                            'valor_original': rec3.valortotal,
                            'medico_id': self.medico_id.id,
                            'valor_medico': valor_con,
                            'valor_glosa': rec3.valorglosa,
                            'valor_imposto': rec3.valortotal * (regra.imposto / 100) if regra.imposto != 0 else 0,
                            'valor_administracao': rec3.valortotal * (
                                    regra.administracao / 100) if regra.administracao != 0 else 0,
                            'valor_repasse': 0 if not regra.especifica_id.repasse_direto else rec3.valortotal - (
                                rec3.valortotal * (regra.imposto / 100) if regra.imposto != 0 else rec3.valortotal * (
                                        regra.administracao / 100)) * (regra.especifica_id.valor_percentual_rep / 100),
                            'usuario_repasse_id': False if not regra.especifica_id.repasse_direto else regra.especifica_id.usuario_destino.id,
                            'doctor_id': rec3.doctor_id.id,  # Acessar o ID do registro relacionado
                        }
                        list_con.append(vals_list_consulta)
                    lista_criada = self.env['consulta'].create(list_con)
                    self.consulta_ids = self.valida_hora(lista_criada,regra)
