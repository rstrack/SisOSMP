from PyQt6 import QtWidgets

from model.modelo import *

from ui.telaCadastroPeca import TelaCadastroPeca
from ui.telaConsultaPecaServico import TelaConsultaPecaServico

class PecaController():
    def __init__(self):
        self.viewCadastro = TelaCadastroPeca()
        self.viewConsulta = TelaConsultaPecaServico()

    def limparCampos(self):
        for lineedit in self.viewCadastro.framedados.findChildren(QtWidgets.QLineEdit):
            lineedit.clear()

    def salvarPecas(self, viewCadastro):
        pecas = []
        if len(viewCadastro.linhasPeca) == 1 and not (viewCadastro.lineEditNomePeca.text() and viewCadastro.lineEditValorPeca.text()):
            raise Exception("Erro: campos vazios!")
        for desc, _, un, valor in viewCadastro.linhasPeca:
            if desc.text() and valor.text():
                qPeca = Peca.select().where(Peca.descricao==desc)
                if not qPeca:
                    aux = valor.text().replace(',','',1)
                    if aux.isdigit():
                        pecas.append(Peca.create(descricao=desc.text(), un=un.currentText(), valor=valor.text().replace(',','.',1)))
                    else: raise Exception("Erro: digite apenas números no valor!")
                else: pecas.append(qPeca[0])
            elif desc.text() or valor.text():
                raise Exception("Preencha todos os campos!")
        return pecas

    def _salvarPecas(self):
        with db.atomic() as transaction:
            try:
                if len(self.viewCadastro.linhasPeca) == 1 and not (self.viewCadastro.lineEditNomePeca.text() and self.viewCadastro.lineEditvalor.text()):
                    raise Exception("Erro: campos vazios!")
                for desc, valor in self.viewCadastro.linhasPeca:
                    if desc.text() and valor.text():
                        aux = valor.text().replace(',','',1)
                        if aux.isdigit():
                            Peca.create(descricao=desc.text(), valor=valor.text().replace(',','.',1))
                        else: raise Exception("Erro: digite apenas números no valor!")
                    elif desc.text() or valor.text():
                        raise Exception("Preencha todos os campos!")
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setText("Dados inseridos!")
                msg.exec()
            except Exception as e:
                transaction.rollback()
                msg =  QtWidgets.QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText(str(e))
                msg.exec()

    def listarPecas(self):
        pass
