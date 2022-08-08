from PyQt6 import QtWidgets
from model.modelo import *

class VeiculoController():
    def __init__(self, tela):
        super(VeiculoController, self).__init__()
        self.tela = tela

    def salvarVeiculo(self):
        veiculo = self.tela.getDadosVeiculo()
        marca = veiculo.pop('marca')
        qMarca = Marca.select().where(Marca.marca==marca)
        if not qMarca:
            cMarca = Marca.create(marca=marca)
        else: cMarca = qMarca[0]

        veiculo['marca'] = cMarca
        cVeiculo = Veiculo.create(**veiculo) #SALVA VEICULO
        return cVeiculo

