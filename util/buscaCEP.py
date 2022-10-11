import requests

class BuscaCEP():
    def __init__(self) -> None:
        pass

    def buscarCEP(self, cep):
        try:
            request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep), timeout=5)
            return request.json()
        except:
            return None

