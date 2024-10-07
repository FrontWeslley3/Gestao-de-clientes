# Importa os blueprints das rotas da aplicação
from routes.home import home_route
from routes.cliente import cliente_route

# Importa o banco de dados e o modelo de cliente
from database.database import db
from database.models.cliente import Cliente

# Função principal para configurar a aplicação com rotas e banco de dados
def configure_all(app):
    configure_routes(app)  # Configura as rotas da aplicação
    configure_db()         # Conecta e configura o banco de dados

# Função que registra as rotas (endpoints) na aplicação Flask
def configure_routes(app):
    # Registra a rota home
    app.register_blueprint(home_route)
    # Registra o blueprint de clientes com o prefixo '/clientes'
    app.register_blueprint(cliente_route, url_prefix='/clientes')

# Função para configurar o banco de dados, conectando e criando as tabelas
def configure_db():
    # Conecta ao banco de dados
    db.connect()
    # Cria a tabela Cliente se não existir
    db.create_tables([Cliente])
