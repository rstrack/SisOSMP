import requests


class BuscaCEP:
    def __init__(self) -> None:
        pass

    def buscarCEP(self, cep):
        try:
            request = requests.get(
                f"https://viacep.com.br/ws/{format(cep)}/json/", timeout=5
            )
            return request.json()
        except:
            return None
