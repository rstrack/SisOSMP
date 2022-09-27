import requests

class BuscaCEP():
    def __init__(self) -> None:
        pass

    def buscarCEP(cep):
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        return request.json()

