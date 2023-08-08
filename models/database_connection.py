# models.py

from odoo import models, fields

class DatabaseConnection(models.Model):
    _name = 'database.connection'
    _description = 'Database Connection'

    name = fields.Char(string='Nome', required=True)
    host = fields.Char(string='Servidro', required=True, default='localhost')
    port = fields.Char(string='Porta', required=True, default='5432')
    database_name = fields.Char(string='Base de Dados', required=True)
    username = fields.Char(string='Usuário BD', required=True)
    password = fields.Char(string='Senha BD', required=True)
