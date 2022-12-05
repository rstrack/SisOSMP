from ui.helpMessageBox import HelpMessageBox

HELPCADASTROPECA = \
'''Cadastro de uma ou mais peças. Para cadastrar mais de uma peça, clique no botão "+".
Selecione a unidade de medida que melhor se aplica a peça que vai ser cadastrada.
Preencha os campos e então clique no botão "Salvar". Caso deseje limpar os campos da tela, clique no botão "Limpar".'''

HELPCADASTROSERVICO = \
'''Cadastro de um ou mais serviços (mão de obra). Para cadastrar mais de um serviço, clique no botão "+".
Preencha os campos e então clique no botão "Salvar". Caso deseje limpar os campos da tela, clique no botão "Limpar".'''

HELPCADASTROCLIENTE = \
'''Cadastro de Clientes e/ou veículos. É possível cadastrar somente um cliente, somente um veículo ou ambos.
Para cadastrar somente cliente ou somente veículo, desmarque a caixa localizada no canto superior esquerdo dos dados do cadastro não desejado.
Ao cadastrar um cliente, se estiver com acesso à internet, campos de endereço são completados automaticamente ao inserir o CEP. Senão, preencha os campos de endereço manualmente.
Ao cadastrar um veículo, selecione uma marca de veículo já cadastrada ou cadastre uma nova marca.
Caso cadastre cliente e veículo juntos, será criado um vínculo entre eles, facilitando utilizações futuras.
Caso tente cadastrar um cliente e um veículo de placa já cadastrada, um aviso aparecerá para escolher se deseja vincular este veículo ao cliente ou cancelar o cadastro.
Preencha os campos e então clique no botão "Salvar". Caso deseje limpar os campos da tela, clique no botão "Limpar".'''

HELPCADASTROORCAMENTO = \
'''Cadastro de orçamento de manutenção de veículos. Cadastre um novo cliente e/ou veículo ou selecione um já existente. Ao selecionar, é possível editar seus dados.
Se estiver com acesso à internet, campos de endereço são completados automaticamente ao inserir o CEP. Senão, preencha os campos de endereço manualmente.
Adicione peças e serviços ao orçamento. Necessário pelo menos um serviço. Para adicionar mais peças ou serviços, clique no botão "+" disponível em suas respectivas seções. 
Ao utilizar peças e serviços já cadastrados, haverá a opção de autocompletar as descrições e valores dos mesmos. O cadastro de peças e serviços ainda não cadastrados é feito automaticamente.
Preencha os campos e então clique no botão "Salvar" ou "Salvar e gerar PDF". Caso deseje limpar os campos da tela, clique no botão "Limpar".'''

HELPCONSULTAPECA = \
'''Consulta por peças cadastradas. Para cadastrar uma nova peça, clique no botão "Novo". Para buscar uma peça já cadastrada, pesquise a peça desejada no campo de pesquisa. É possivel selecionar o cadastro, edição ou exclusão de peças.
Exclusão somente é permitida caso a peça não tenha sido usada em nenhum cadastro de orçamento.'''

HELPCONSULTASERVICO = \
'''Consulta por serviços (mão de obra) cadastrados. Para cadastrar um novo serviço, clique no botão "Novo". Para buscar um serviço já cadastrado, pesquise o serviço desejado no campo de pesquisa. É possivel selecionar o cadastro, edição ou exclusão de serviços.
Exclusão somente é permitida caso o serviço não tenha sido usado em nenhum cadastro de orçamento.'''

HELPCONSULTACLIENTE = \
'''Consulta por clientes cadastrados. Para cadastrar um novo cliente, clique no botão "Novo". Para buscar um cliente já cadastrado, pesquise o cliente desejado no campo de pesquisa. É possivel selecionar o cadastro, edição ou exclusão de clientes.
Exclusão somente é permitida caso o cliente não tenha sido usado em nenhum cadastro de orçamento.
Para ver veículos vinculados ao cliente selecionado, clique no botão "Veículos"'''

HELPCONSULTAVEICULO = \
'''Consulta por veículos cadastrados. Para cadastrar um novo veículo, clique no botão "Novo". Para buscar um veículo já cadastrado, pesquise o veículo desejado no campo de pesquisa. É possivel selecionar o cadastro, edição ou exclusão de veículos.
Exclusão somente é permitida caso o veículo não tenha sido usado em nenhum cadastro de orçamento.
Para ver clientes vinculados ao veículo selecionado, clique no botão "Clientes".
Para ver marcas de veículos cadastradas, clique no botão "Marcas".'''

HELPCONSULTAORCAMENTO = \
'''Consulta por orçamentos cadastrados. Para cadastrar um novo orçamento, clique no botão "Novo". Para visualizar um orçamento, selecione seu status (aguardando aprovação ou reprovado) e pesquise-o no campo de pesquisa.. 
Caso o orçamento esteja aguardando aprovação, é possível selecionar as opções de editar, gerar arquivo PDF, aprovar, reprovar ou excluir orçamento. 
Caso o orçamento tenha sido reprovado, somente é possível gerar o arquivo PDF do mesmo.'''

HELPCONSULTAOS = \
'''Consulta por ordens de serviço (orçamentos aprovados). Para visualizar uma ordem de serviço, selecione seu status (finalizada ou não finalizada), pesquise-a no campo de pesquisa e selecione-a.
Caso a ordem de serviço esteja em andamento, é possível selecionar as opções de editar, gerar arquivo PDF, finalizar e excluir.
Caso a ordem de serviço esteja finalizada, somente é possível gerar o arquivo PDF da mesma.'''

HELPEDITARPECA = \
'''Edição de peças cadastradas. Altere os dados da peça selecionada e então clique no botão "Salvar" para que as modificações sejam salvas. 
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPEDITARSERVICO = \
'''Edição de serviços cadastrados. Altere os dados do serviço selecionado e então clique no botão "Salvar" para que as modificações sejam salvas. 
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPEDITARCLIENTE = \
'''Edição de clientes cadastrados. Modifique as informações do cliente selecionado e então clique no botão "Salvar" para que as modificações sejam salvas.
Se estiver com acesso à internet, campos de endereço são completados automaticamente ao inserir o CEP. Senão, preencha os campos de endereço manualmente.
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPEDITARVEICULO = \
'''Edição de veículo cadastrados. Altere os dados do veículo selecionado e então clique no botão "Salvar" para que as modificações sejam salvas. 
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPEDITARORCAMENTO = \
'''Edição de orçamentos cadastrados. Altere peças e serviços do orçamento, além dos campos de data e quilometragem. Caso deseje alterar os dados do cliente e/ou veículo, é necessário ir em suas próprias páginas de edição.
Ao utilizar peças e serviços já cadastrados, haverá a opção de autocompletar as descrições e valores dos mesmos. O cadastro de peças e serviços ainda não cadastrados é feito automaticamente.
Após realizar as edições, clique no botão "Salvar". Caso queira salvar edições e gerar o arquivo PDF do orçamento clique no botão "Salvar e gerar PDF".
Se o cliente aprovar o orçamento, clique no botão "Editar e Aprovar", caso contrário, clique no botão "Reprovar".
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPEDITAROS = \
'''Edição de ordens de serviço cadastradas. Altere peças e serviços da ordem de serviço, além dos campos de data e quilometragem. Caso deseje alterar os dados do cliente e/ou veículo, é necessário ir em suas próprias páginas de edição.
Ao utilizar peças e serviços já cadastrados, haverá a opção de autocompletar as descrições e valores dos mesmos. O cadastro de peças e serviços ainda não cadastrados é feito automaticamente.
Após realizar as edições, clique no botão "Salvar". Caso queira salvar edições e gerar o arquivo PDF da ordem de serviço, clique no botão "Salvar e gerar PDF".
Se a ordem de serviço for concluída, clique no botão "Finalizar".
Caso não deseje mais realizar a edição, clique no botão "Cancelar".'''

HELPBUSCACLIENTE = \
'''Busca por cliente. Pesquise e selecione o cliente desejado, então clique no botão "selecionar" para utilizá-lo no orçamento.
Caso o cliente possua somente um veículo vinculado a ele, este veículo será automaticamente selecionado.'''

HELPBUSCAVEICULO = \
'''Busca por veículo. Pesquise e selecione o veículo desejado, então clique no botão "selecionar" para utilizá-lo no orçamento.'''

HELPVEICULOS_CLIENTE = \
'''Veículos vinculados a um cliente. É possivel desvincular veículos de um cliente. O vínculo pode ser refeito ao cadastrar um orçamento com os cliente e veículo em questão.'''

HELPCLIENTES_VEICULO = \
'''Clientes vinculados a um veículo. É possivel desvincular clientes de um veículo. O vínculo pode ser refeito ao cadastrar um orçamento com os cliente e veículo em questão.'''

HELPMARCAS = \
'''Marcas de veículos. É possivel realizar a edição ou exclusão de uma marca. Exclusão somente é permitida caso a marca não possua nenhum veículo cadastrado.'''

def help(title:str, body:str, width=None):
    msg = HelpMessageBox()
    msg.setWindowTitle(title)
    if width: msg.setFixedWidth(width)
    msg.setMessage(body)
    msg.exec()

