# Importando as bibliotecas necessárias do Flask
from flask import Blueprint, render_template

# Criando um objeto Blueprint chamado 'home'
home_route = Blueprint('home', __name__)

# Definindo a rota para a página inicial
@home_route.route('/')
def home():
    # Renderiza o template 'index.html' quando a rota raiz é acessada
    return render_template('index.html')
