import requests

class BuscaCEP:
    @staticmethod
    def buscarCEP(cep):
        try:
            request = requests.get(
                f"https://viacep.com.br/ws/{format(cep)}/json/", timeout=5
            )
            return request.json()
        except:
            return None
