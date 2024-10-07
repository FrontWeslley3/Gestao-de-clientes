# Importando as classes necessárias do peewee
from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Cliente(Model):
    # Definindo os campos do modelo
    nome = CharField()  # Campo para o nome do cliente
    email = CharField()  # Campo para o email do cliente
    telefone = CharField(max_length=15)  # Limite de 15 caracteres para o número de telefone
    data_registro = DateTimeField(default=datetime.datetime.now)  # Data de registro padrão é a data atual

    class Meta:
        database = db  # Especificando que o banco de dados utilizado é o definido em database.py
