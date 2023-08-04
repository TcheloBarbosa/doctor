from odoo import models, fields, api
from sqlalchemy import create_engine, MetaData, Table, between, join, and_, select
from sqlalchemy.orm import sessionmaker


class PacientesContasProcedimento(models.TransientModel):
    _name = 'pacientes.contas.procedimentos'
    _description = 'Pacientes Contas Procedimentos'

    doctor_id = fields.Many2one('doctor', string='Doctor')
    convenio_id = fields.Many2one('convenios', string="Convenio")
    medico_id = fields.Many2one('usuarios', string="Médico")
    conta = fields.Char(string='Conta')
    #conta = fields.Many2one('pacientes.contas', string="Conta")
    linha = fields.Char(string='Linha')
    data = fields.Date(string='Data')
    horainicial = fields.Char(string='Hora Inicial')
    horafinal = fields.Char(string='Hora Final')
    indice = fields.Char(string='Índice')
    indicehonorariosamb = fields.Float(string='Índice Honorários AMB')
    indicecustooperacionalamb = fields.Float(string='Índice Custo Operacional AMB')
    indicecustooperacionalcbhpm = fields.Float(string='Índice Custo Operacional CBHPM')
    indicem2filme = fields.Float(string='Índice M2 Filme')
    indiceportecbhpm = fields.Float(string='Índice Porte CBHPM')
    local = fields.Char(string='Local')
    usuario = fields.Char(string='Usuário')
    percusuario_1 = fields.Float(string='Percentual Usuário 1')
    percusuario_2 = fields.Float(string='Percentual Usuário 2')
    percusuario_3 = fields.Float(string='Percentual Usuário 3')
    percusuario_4 = fields.Float(string='Percentual Usuário 4')
    funcao = fields.Char(string='Função')
    codigoamb = fields.Char(string='Código AMB')
    descricaoamb = fields.Char(string='Descrição AMB')
    quantidade = fields.Float(string='Quantidade')
    quantidadesolicitada = fields.Float(string='Quantidade Solicitada')
    quantidadeautorizada = fields.Float(string='Quantidade Autorizada')
    tipoguia = fields.Char(string='Tipo Guia')
    guia = fields.Char(string='Guia')
    guiacancelada = fields.Char(string='Guia Cancelada')
    tipoprocedimento = fields.Char(string='Tipo Procedimento')
    inc = fields.Char(string='INC')
    m2filme = fields.Char(string='M2 Filme')
    custooperacional = fields.Float(string='Custo Operacional')
    porteprocedimento = fields.Char(string='Porte Procedimento')
    porteprocedimentoindice = fields.Float(string='Porte Procedimento Índice')
    honorario = fields.Float(string='Honorário')
    numauxiliares = fields.Integer(string='Número de Auxiliares')
    porteanestesico = fields.Float(string='Porte Anestésico')
    porteanestesicoindice = fields.Float(string='Porte Anestésico Índice')
    cirurgiabilateral = fields.Char(string='Cirurgia Bilateral')
    cirurgiamesmavia = fields.Char(string='Cirurgia Mesma Via')
    cirurgiaviadiferente = fields.Char(string='Cirurgia Via Diferente')
    urgencia = fields.Char(string='Urgência')
    dhe = fields.Char(string='DHE')
    tecnicautilizada = fields.Char(string='Técnica Utilizada')
    apartamento = fields.Char(string='Apartamento')
    solicitado = fields.Float(string='Solicitado')
    pendencia = fields.Float(string='Pendência')
    realizado = fields.Float(string='Realizado')
    glosado = fields.Float(string='Glosado')
    valorglosa = fields.Float(string='Valor Glosa')
    diferenca = fields.Float(string='Diferença')
    valordiferenca = fields.Float(string='Valor Diferença')
    valortotal = fields.Float(string='Valor Total')
    solicitante = fields.Char(string='Solicitante')
    solicitante_nome = fields.Char(string='Nome do Solicitante')
    solicitante_especialidade = fields.Char(string='Especialidade do Solicitante')
    solicitante_conselhotipo = fields.Char(string='Tipo Conselho do Solicitante')
    solicitante_conselhonumero = fields.Char(string='Número do Conselho do Solicitante')
    solicitante_conselhouf = fields.Char(string='UF do Conselho do Solicitante')
    protocoloenvio = fields.Char(string='Protocolo de Envio')
    loteenvio = fields.Char(string='Lote de Envio')
    situacaotransacao = fields.Char(string='Situação da Transação')
    autorizacaotransacao = fields.Char(string='Autorização da Transação')
    tickettransacao = fields.Char(string='Ticket da Transação')
    mensagemtransacao = fields.Char(string='Mensagem da Transação')
    data_rec = fields.Char(string='Data REC')
    valor_rec = fields.Float(string='Valor REC')
    situacao_rec = fields.Char(string='Situação REC')
    repassado_rec = fields.Float(string='Repassado REC')
    recebido_rec = fields.Float(string='Recebido REC')
    codigotuss = fields.Char(string='Código TUSS')
    descricaotuss = fields.Char(string='Descrição TUSS')
    valorrecursado = fields.Float(string='Valor Recursado')
    valorrecuperado = fields.Float(string='Valor Recuperado')
    funcaorepasse = fields.Char(string='Função Repasse')
    numrepasse = fields.Char(string='Número Repasse')
    tipovalorrepasse_hono = fields.Char(string='Tipo Valor Repasse Honorário')
    valoraplicadorepasse_hono = fields.Float(string='Valor Aplicado Repasse Honorário')
    valorrepasse = fields.Float(string='Valor Repasse')
    previa = fields.Char(string='Prévia')
    tppagamento = fields.Char(string='Tipo de Pagamento')
    valorimpostosrepasse = fields.Float(string='Valor Impostos Repasse')
    valorrepasse_hono = fields.Float(string='Valor Repasse Honorário')
    valorimpostosrepasse_hono = fields.Float(string='Valor Impostos Repasse Honorário')
    tipovalorrepasse_custoop = fields.Char(string='Tipo Valor Repasse Custo Operacional')
    valoraplicadorepasse_custoop = fields.Float(string='Valor Aplicado Repasse Custo Operacional')
    valorrepasse_custoop = fields.Float(string='Valor Repasse Custo Operacional')
    valorimpostosrepasse_custoop = fields.Float(string='Valor Impostos Repasse Custo Operacional')
    tipovalorrepasse_m2filme = fields.Char(string='Tipo Valor Repasse M2 Filme')
    valoraplicadorepasse_m2filme = fields.Float(string='Valor Aplicado Repasse M2 Filme')
    valorrepasse_m2filme = fields.Float(string='Valor Repasse M2 Filme')
    valorimpostosrepasse_m2filme = fields.Float(string='Valor Impostos Repasse M2 Filme')
    valorprocedimento_hono = fields.Float(string='Valor Procedimento Honorário')
    valorprocedimento_m2filme = fields.Float(string='Valor Procedimento M2 Filme')
    valorprocedimento_custoop = fields.Float(string='Valor Procedimento Custo Operacional')
    linharefrepasse = fields.Char(string='Linha Referência Repasse')
    tiss3_numeroguiaoperadora = fields.Char(string='Número Guia Operadora TISS3')
    tiss3_tabela = fields.Char(string='Tabela TISS3')
    codigoespecifico = fields.Char(string='Código Específico')
    descricaoespecifica = fields.Char(string='Descrição Específica')
    naoincluirrepasse = fields.Char(string='Não Incluir Repasse')
    procedimentosomenterepasse = fields.Char(string='Procedimento Somente Repasse')
    procedimentoassociado = fields.Char(string='Procedimento Associado')
    linhaassociada = fields.Char(string='Linha Associada')
    contaassociada = fields.Char(string='Conta Associada')
    tratamentofinalizado = fields.Char(string='Tratamento Finalizado')
    valortotalsemredacresc = fields.Float(string='Valor Total sem Redução de Acréscimo')
    valortotalsomenterepasse = fields.Float(string='Valor Total Somente Repasse')
    anotacoes = fields.Char(string='Anotações')
    procedimentoassociavel = fields.Char(string='Procedimento Associável')
    recebeassociacao = fields.Char(string='Recebe Associação')
    naorepassar = fields.Char(string='Não Repassar')
    fatorcorrecaohonorario = fields.Float(string='Fator Correção Honorário')
    fatorcorrecaoco = fields.Float(string='Fator Correção CO')
    usuarioespecialidade = fields.Char(string='Especialidade do Usuário')
    usuarioconselhotipo = fields.Char(string='Tipo Conselho do Usuário')
    usuarioconselhonumero = fields.Char(string='Número do Conselho do Usuário')
    usuarioconselhouf = fields.Char(string='UF do Conselho do Usuário')
    tipodiferenca = fields.Char(string='Tipo Diferença')
    percdiferenca = fields.Float(string='Percentual Diferença')

    def get_external_data(self, incio, fim, medico, convenio):
        db_host = 'localhost'
        db_port = '5432'
        db_name = 'prodoc'
        db_user = 'postgres'
        db_password = '450450'
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        metadata = MetaData()
        Session = sessionmaker(bind=engine)
        session = Session()
        table = Table('t_pacientescontasprocedimentos', metadata, autoload_with=engine)
        outra_table = Table('t_pacientescontas', metadata, autoload_with=engine)
        conditions = between(table.c.data, incio, fim)
        join_condition = table.c.conta == outra_table.c.conta
        if convenio and medico:
            convenio_cond = outra_table.c.convenio == convenio
            medico_cond = outra_table.c.usuario == medico
            condicoes_multiplas = and_(conditions, convenio_cond, medico_cond)
            query = select([table, outra_table]).join(outra_table, join_condition).where(condicoes_multiplas)
            result = session.execute(query).fetchall()
        elif convenio and not medico:
            convenio_cond = outra_table.c.convenio == convenio
            condicoes_multiplas = and_(conditions, convenio_cond)
            query = select([table, outra_table]).join(outra_table, join_condition).where(condicoes_multiplas)
            result = session.execute(query).fetchall()
        elif medico and not convenio:
            medico_cond = outra_table.c.usuario == medico
            condicoes_multiplas = and_(conditions, medico_cond)
            query = select([table, outra_table]).join(outra_table, join_condition).where(condicoes_multiplas)
            result = session.execute(query).fetchall()
        else:
            result = session.query(table).filter(conditions).all()

        data = []
        for row in result:
            data.append({
                'conta': row.conta,
                'linha': row.linha,
                'data': row.data,
                'convenio_id': int(self.env['convenios'].search([('codigo_prodoctor', '=', row.convenio)], limit=1).id) if not convenio else self.env['convenios'].search([('codigo_prodoctor', '=', convenio)], limit=1).id,
                'medico_id': int(self.env['usuarios'].search([('codigo_prodoctor', '=', row.usuario)], limit=1).id) if not medico else self.env['usuarios'].search([('codigo_prodoctor', '=', medico)], limit=1).id,
                'horainicial': row.horainicial,
                'horafinal': row.horafinal,
                'indice': row.indice,
                'indicehonorariosamb': row.indicehonorariosamb,
                'indicecustooperacionalamb': row.indicecustooperacionalamb,
                'indicecustooperacionalcbhpm': row.indicecustooperacionalcbhpm,
                'indicem2filme': row.indicem2filme,
                'indiceportecbhpm': row.indiceportecbhpm,
                'local': row.local,
                'usuario': row.usuario,
                'percusuario_1': row.percusuario_1,
                'percusuario_2': row.percusuario_2,
                'percusuario_3': row.percusuario_3,
                'percusuario_4': row.percusuario_4,
                'funcao': row.funcao,
                'codigoamb': row.codigoamb,
                'descricaoamb': row.descricaoamb,
                'quantidade': row.quantidade,
                'quantidadesolicitada': row.quantidadesolicitada,
                'quantidadeautorizada': row.quantidadeautorizada,
                'tipoguia': row.tipoguia,
                'guia': row.guia,
                'guiacancelada': row.guiacancelada,
                'tipoprocedimento': row.tipoprocedimento,
                'inc': row.inc,
                'm2filme': row.m2filme,
                'custooperacional': row.custooperacional,
                'porteprocedimento': row.porteprocedimento,
                'porteprocedimentoindice': row.porteprocedimentoindice,
                'honorario': row.honorario,
                'numauxiliares': row.numauxiliares,
                'porteanestesico': row.porteanestesico,
                'porteanestesicoindice': row.porteanestesicoindice,
                'cirurgiabilateral': row.cirurgiabilateral,
                'cirurgiamesmavia': row.cirurgiamesmavia,
                'cirurgiaviadiferente': row.cirurgiaviadiferente,
                'urgencia': row.urgencia,
                'dhe': row.dhe,
                'tecnicautilizada': row.tecnicautilizada,
                'apartamento': row.apartamento,
                'solicitado': row.solicitado,
                'pendencia': row.pendencia,
                'realizado': row.realizado,
                'glosado': row.glosado,
                'valorglosa': row.valorglosa,
                'diferenca': row.diferenca,
                'valordiferenca': row.valordiferenca,
                'valortotal': row.valortotal,
                'solicitante': row.solicitante,
                'solicitante_nome': row.solicitante_nome,
                'solicitante_especialidade': row.solicitante_especialidade,
                'solicitante_conselhotipo': row.solicitante_conselhotipo,
                'solicitante_conselhonumero': row.solicitante_conselhonumero,
                'solicitante_conselhouf': row.solicitante_conselhouf,
                'protocoloenvio': row.protocoloenvio,
                'loteenvio': row.loteenvio,
                'situacaotransacao': row.situacaotransacao,
                'autorizacaotransacao': row.autorizacaotransacao,
                'tickettransacao': row.tickettransacao,
                'mensagemtransacao': row.mensagemtransacao,
                'data_rec': row.data_rec,
                'valor_rec': row.valor_rec,
                'situacao_rec': row.situacao_rec,
                'repassado_rec': row.repassado_rec,
                'recebido_rec': row.recebido_rec,
                'codigotuss': row.codigotuss,
                'descricaotuss': row.descricaotuss,
                'valorrecursado': row.valorrecursado,
                'valorrecuperado': row.valorrecuperado,
                'funcaorepasse': row.funcaorepasse,
                'numrepasse': row.numrepasse,
                'tipovalorrepasse_hono': row.tipovalorrepasse_hono,
                'valoraplicadorepasse_hono': row.valoraplicadorepasse_hono,
                'valorrepasse': row.valorrepasse,
                'previa': row.previa,
                'tppagamento': row.tppagamento,
                'valorimpostosrepasse': row.valorimpostosrepasse,
                'valorrepasse_hono': row.valorrepasse_hono,
                'valorimpostosrepasse_hono': row.valorimpostosrepasse_hono,
                'tipovalorrepasse_custoop': row.tipovalorrepasse_custoop,
                'valoraplicadorepasse_custoop': row.valoraplicadorepasse_custoop,
                'valorrepasse_custoop': row.valorrepasse_custoop,
                'valorimpostosrepasse_custoop': row.valorimpostosrepasse_custoop,
                'tipovalorrepasse_m2filme': row.tipovalorrepasse_m2filme,
                'valoraplicadorepasse_m2filme': row.valoraplicadorepasse_m2filme,
                'valorrepasse_m2filme': row.valorrepasse_m2filme,
                'valorimpostosrepasse_m2filme': row.valorimpostosrepasse_m2filme,
                'valorprocedimento_hono': row.valorprocedimento_hono,
                'valorprocedimento_m2filme': row.valorprocedimento_m2filme,
                'valorprocedimento_custoop': row.valorprocedimento_custoop,
                'linharefrepasse': row.linharefrepasse,
                'tiss3_numeroguiaoperadora': row.tiss3_numeroguiaoperadora,
                'tiss3_tabela': row.tiss3_tabela,
                'codigoespecifico': row.codigoespecifico,
                'descricaoespecifica': row.descricaoespecifica,
                'naoincluirrepasse': row.naoincluirrepasse,
                'procedimentosomenterepasse': row.procedimentosomenterepasse,
                'procedimentoassociado': row.procedimentoassociado,
                'linhaassociada': row.linhaassociada,
                'contaassociada': row.contaassociada,
                'tratamentofinalizado': row.tratamentofinalizado,
                'valortotalsemredacresc': row.valortotalsemredacresc,
                'valortotalsomenterepasse': row.valortotalsomenterepasse,
                'anotacoes': row.anotacoes,
                'procedimentoassociavel': row.procedimentoassociavel,
                'recebeassociacao': row.recebeassociacao,
                'naorepassar': row.naorepassar,
                'fatorcorrecaohonorario': row.fatorcorrecaohonorario,
                'fatorcorrecaoco': row.fatorcorrecaoco,
                'usuarioespecialidade': row.usuarioespecialidade,
                'usuarioconselhotipo': row.usuarioconselhotipo,
                'usuarioconselhonumero': row.usuarioconselhonumero,
                'usuarioconselhouf': row.usuarioconselhouf,
                'tipodiferenca': row.tipodiferenca,
                'percdiferenca': row.percdiferenca,
            })
        return data
