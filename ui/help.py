from ui.helpMessageBox import HelpMessageBox

HELPCADASTROPECA = \
''''''

HELPCADASTROSERVICO = \
''''''

HELPCADASTROCLIENTE = \
''''''

HELPCADASTROORCAMENTO = \
'''Cadastro de orçamento de manutenção de veículos. Cadastre um novo cliente e/ou veículo ou selecione um já existente. Ao selecionar, é possível editar seus dados.
Se estiver com acesso à internet, campos de endereço são completados automaticamente ao inserir o CEP.
Adicione peças e serviços ao orçamento. Necessário pelo menos um serviço. Para adicionar mais peças ou serviços, clique no botão "+" disponível em suas respectivas seções.
Após concluir, selecione a opção de salvar somente ou salvar e gerar o arquivo PDF para visualização do orçamento.'''

HELPCONSULTAPECA = \
''''''

HELPCONSULTASERVICO = \
''''''

HELPCONSULTACLIENTE = \
''''''

HELPCONSULTAVEICULO = \
''''''

HELPCONSULTAORCAMENTO = \
''''''

HELPCONSULTAOS = \
''''''

HELPEDITARPECA = \
''''''

HELPEDITARSERVICO = \
''''''

HELPEDITARCLIENTE = \
''''''

HELPEDITARVEICULO = \
''''''

HELPEDITARORCAMENTO = \
''''''

HELPEDITAROS = \
''''''

HELPBUSCACLIENTE = \
''''''

HELPBUSCAVEICULO = \
''''''

HELPVEICULOCLIENTE = \
''''''

HELPMARCAS = \
''''''

def help(title:str, body:str):
    msg = HelpMessageBox()
    msg.setWindowTitle(title)
    msg.setMessage(body)
    msg.exec()