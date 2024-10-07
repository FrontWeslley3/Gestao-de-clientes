# Importa a biblioteca Flask para criar a aplicação web
from flask import Flask
# Importa a função 'configure_all' para configurar rotas e banco de dados
from configuration import configure_all

# Cria a instância da aplicação Flask, que será usada para definir as rotas e configurações
app = Flask(__name__)

# Chama a função 'configure_all' para registrar todas as rotas e a configuração do banco de dados
configure_all(app)

# Inicia a aplicação com o modo 'debug' ativado para facilitar o desenvolvimento
app.run(debug=True)
