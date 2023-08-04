from odoo import models, fields, api

class PacientesContas(models.Model):
    _name = 'pacientes.contas'
    _description = 'Pacientes Contas'

    # Fields
    datahoraentrada = fields.Datetime(string='Data e Hora de Entrada')
    numeromatricula = fields.Char(string='Número Matrícula')
    codigoamb = fields.Char(string='Código AMB')
    descricaoamb = fields.Char(string='Descrição AMB')
    totalmateriais = fields.Float(string='Total Materiais')
    totalglosasmateriais = fields.Float(string='Total Glosas Materiais')
    totalmedicamentos = fields.Float(string='Total Medicamentos')
    totalglosasmedicamentos = fields.Float(string='Total Glosas Medicamentos')
    totaltaxas = fields.Float(string='Total Taxas')
    totalglosastaxas = fields.Float(string='Total Glosas Taxas')
    totaldiarias = fields.Float(string='Total Diárias')
    totalglosasdiarias = fields.Float(string='Total Glosas Diárias')
    totalgases = fields.Float(string='Total Gases')
    totalglosasgases = fields.Float(string='Total Glosas Gases')
    conta = fields.Char(string='Conta')
    fatura = fields.Char(string='Fatura')
    paciente_id = fields.Many2one('pacientes', string='Paciente')
    usuario_id = fields.Many2one('usuarios', string='Médico')
    convenio_id = fields.Many2one('convenios', string='Convênio', compute='_compute_convenio_id', store=True)
    codigo_prodoctor = fields.Integer(string="Código ProDoctor")
    procedimentos_ids = fields.One2many('pacientes.contas.procedimentos', 'conta_id', string='Procedimentos')

    # Computed fields
    @api.depends('totalmateriais', 'totalglosasmateriais', 'totalmedicamentos', 'totalglosasmedicamentos')
    def _compute_totalmatmed(self):
        for record in self:
            record.totalmatmed = record.totalmateriais + record.totalglosasmateriais + record.totalmedicamentos + record.totalglosasmedicamentos

    @api.depends('totaltaxas', 'totalglosastaxas', 'totaldiarias', 'totalglosasdiarias', 'totalgases', 'totalglosasgases')
    def _compute_totaltaxas(self):
        for record in self:
            record.totaltaxas = record.totaltaxas + record.totalglosastaxas + record.totaldiarias + record.totalglosasdiarias + record.totalgases + record.totalglosasgases

    @api.depends('totalmatmed', 'totaltaxas')
    def _compute_totalgeral(self):
        for record in self:
            record.totalgeral = record.totalmatmed + record.totaltaxas

    @api.depends('codigo_prodoctor')
    def _compute_convenio_id(self):
        for conta in self:
            convenio = self.env['convenios'].search([('codigo_prodoctor', '=', conta.codigo_prodoctor)], limit=1)
            if convenio:
                conta.convenio_id = convenio
            else:
                conta.convenio_id = False
