from odoo import models, api, fields


# class DoctorWizard(models.TransientModel):
#     _name = 'doctor.wizard'
#
#     def get_external_data(self):
#         print(self)
#         self.env['doctor'].get_external_data()
#         return {}
class DoctorWizard(models.TransientModel):
    _name = 'doctor.wizard'
    line_ids = fields.One2many('doctor.wizard.line', 'wizard_id', string='Lines')

    def get_external_data(self):
        self.line_ids.unlink()  # remove any existing lines
        external_data = self.env['doctor'].get_external_data()
        lines = [(0, 0, row) for row in external_data]
        self.line_ids = lines
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'doctor.wizard',  # same model as the wizard
            'view_mode': 'form',
            'res_id': self.id,  # ID of the current wizard record
            'target': 'new',  # opens in a new window
            'context': self.env.context,  # pass current context to keep the data
        }
# class DoctorWizard(models.TransientModel):
#     _name = 'doctor.wizard'
#
#     line_ids = fields.One2many('doctor.wizard.line', 'wizard_id')
    # def get_external_data(self):
    #     self.line_ids.unlink()  # remove any existing lines
    #
    #     db_host = 'localhost'
    #     db_port = '5432'
    #     db_name = 'postgres'
    #     db_user = 'postgres'
    #     db_password = '450450'
    #     engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    #     metadata = MetaData()
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #     table = Table('t_dadogerais', metadata, autoload_with=engine)
    #     result = session.query(table).all()
    #
    #     lines = [(0, 0, {'id': row.id, 'nome': row.nome, 'senha': row.senha, 'alinhamento': row.alinhamento}) for row in result]
    #     self.line_ids = lines
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'doctor.wizard',  # same model as the wizard
    #         'view_mode': 'form',
    #         'res_id': self.id,  # ID of the current wizard record
    #         'target': 'new',  # opens in a new window
    #         'context': self.env.context,  # pass current context to keep the data
    #     }

class DoctorWizardLine(models.TransientModel):
    _name = 'doctor.wizard.line'

    wizard_id = fields.Many2one('doctor.wizard', string='Wizard')
    id = fields.Integer(string='ID')
    nome = fields.Text(string='Nome')
    senha = fields.Text(string='Senha')
    alinhamento = fields.Text(string='Alinhamento')
