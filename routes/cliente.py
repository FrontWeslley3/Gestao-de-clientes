# Importando as bibliotecas necessárias do Flask
from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

# Criando um objeto Blueprint chamado 'cliente'
cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ Listar os clientes """
    clientes = Cliente.select()  # Seleciona todos os clientes do banco de dados
    return render_template('lista_clientes.html', clientes=clientes)  # Renderiza o template com a lista de clientes

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente """
    data = request.json  # Obtém os dados do cliente no formato JSON da requisição
    
    novo_usuario = Cliente.create(
        nome=data['nome'],     # Cria um novo cliente com os dados recebidos
        email=data['email'],
        telefone=data['telefone'],
    )
    
    return render_template('item_cliente.html', cliente=novo_usuario)  # Renderiza o template do cliente inserido

@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template('form_cliente.html')  # Renderiza o formulário de cadastro

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes do cliente """
    cliente = Cliente.get_by_id(cliente_id)  # Obtém os dados do cliente pelo ID
    return render_template('detalhe_cliente.html', cliente=cliente)  # Renderiza o template com os detalhes do cliente

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulário para editar um cliente """
    cliente = Cliente.get_by_id(cliente_id)  # Obtém os dados do cliente pelo ID para edição
    return render_template('form_cliente.html', cliente=cliente)  # Renderiza o formulário de edição

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar informações do cliente """
    data = request.json  # Obtém os dados do formulário de edição em JSON

    cliente_editado = Cliente.get_by_id(cliente_id)  # Obtém o cliente pelo ID
    cliente_editado.nome = data['nome']  # Atualiza os dados do cliente
    cliente_editado.email = data['email']
    cliente_editado.telefone = data['telefone']
    cliente_editado.save()  # Salva as alterações no banco de dados
            
    return render_template('item_cliente.html', cliente=cliente_editado)  # Renderiza o template do cliente atualizado

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    cliente = Cliente.get_by_id(cliente_id)  # Obtém o cliente pelo ID
    cliente.delete_instance()  # Remove o cliente do banco de dados
    return {'deleted': 'ok'}  # Retorna uma confirmação de deleção
