import requests

class BuscaCEP():

    def buscarCEP(cep):
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        return request.json()

