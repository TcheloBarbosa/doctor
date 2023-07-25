from odoo import models, fields
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


class Doctor(models.Model):
    _name = 'doctor'

    id = fields.Integer(string='ID')
    nome = fields.Text(string='Nome')
    senha = fields.Text(string='Senha')
    alinhamento = fields.Text(string='Alinhamento')

    def get_external_data(self):
        db_host = 'localhost'
        db_port = '5432'
        db_name = 'postgres'
        db_user = 'postgres'
        db_password = '450450'
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        metadata = MetaData()
        Session = sessionmaker(bind=engine)
        session = Session()
        table = Table('t_dadogerais',metadata, autoload_with=engine)
        result = session.query(table).all()

        data= []
        for row in result:
            data.append({
                'id': row.id,
                'nome': row.nome,
                'senha': row.senha,
                'alinhamento': row.alinhamento,
            })
        return data


