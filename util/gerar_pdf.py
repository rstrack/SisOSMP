from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import textwrap
import os


# DICT DO ORÇAMENTO GERADO AO SALVAR/EDITAR
# Configurações para geração do pdf
def tabelas_pos(self, orcamento: dict, l, g):
    self.setFont('Helvetica', 10)
    self.drawString(395, l + 4, 'Valor Total das Peças:')
    self.rect(390, l, 1 * inch + 51, 15, fill=False, stroke=True)
    self.rect(441 + 1 * inch, l, 1 * inch, 15, fill=False, stroke=True)
    self.drawString(395, l - 11, 'Valor Total dos Serviços:')
    self.rect(390, l - 15, 1 * inch + 51, 15, fill=False, stroke=True)
    self.rect(441 + 1 * inch, l - 15, 1 * inch, 15, fill=False, stroke=True)
    self.drawString(395, l - 26, 'Valor Total')
    self.drawString(570 - (len(str(orcamento['valorTotal'])) * 7.1), l - 26,
                    'R$ {:.2f}'.format(orcamento['valorTotal']))
    self.rect(390, l - 30, 1 * inch + 51, 15, fill=False, stroke=True)
    self.rect(441 + 1 * inch, l - 30, 1 * inch, 15, fill=False, stroke=True)
    self.drawString(265, g + 4, 'Observações:')
    linhas = orcamento['observacoes'].split('\n')
    linhasObs = []
    for linha in linhas:
        linhasObs.extend(textwrap.wrap(linha, 100, break_long_words=False))
    c = 123
    q = g - 11
    # pular linha em observações(vai ser melhorado ainda)
    for x in linhasObs:
        self.drawString(30, q, x)
        c = c + 103
        q = q - 15
    self.rect(10, g, 575, 15, fill=False, stroke=True)
    self.rect(10, g - 60, 575, 60, fill=False, stroke=True)


def generatePDF(orcamento: dict, listaFones: list[dict], listaServicos: list[dict], listaPecas: list[dict] = None, path:str = None):
    if path:
        pdf = canvas.Canvas(f"{path}\\teste.pdf", pagesize=A4)
    else:
        pdf = canvas.Canvas(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\teste.pdf", pagesize=A4)
    pdf.drawInlineImage(
        "./resources/logo2.png", 0, 740, 200, 100
    )
    pdf.setFont('Helvetica-Bold', 10)
    stylesheet = getSampleStyleSheet()
    pdf.normalStyle = stylesheet['Normal']
    # Cabeçalho padrão do pdf
    pdf.drawString(312, 810, 'Fone: (42) 3027-4990 / (42) 4141-1755')
    pdf.drawString(260, 800, 'Rua Barão do Bojuru, Nº 87 - Ronda - Ponta Grossa - PR')
    pdf.drawString(335, 790, 'CNPJ : 85.481.562/0001-57')
    pdf.drawString(315, 780, 'E-mail:mecanicapasetto@gmail.com ')
    pdf.rect(10, 750, 575, 2, fill=True, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    # Informações do Cliente

    pdf.drawString(255, 713, 'Dados do Cliente')

    pdf.setFont('Helvetica', 10)
    pdf.drawString(20, 729, 'Data: {}'.format(orcamento['dataOrcamento'].strftime("%d/%m/%Y")))
    pdf.rect(10, 725, 97, 15, fill=False, stroke=True)
    pdf.rect(10, 710, 575, 15, fill=False, stroke=True)
    pdf.drawString(20, 699, 'Nome: {}'.format(orcamento['cliente']['nome']))
    pdf.rect(10, 695, 575, 15, fill=False, stroke=True)
    if orcamento['cliente']['tipo'] == '0':
        documento = 'CPF'
    elif orcamento['cliente']['tipo'] == '1':
        documento = 'CNPJ'
    else:
        documento = 'Documento'
    pdf.drawString(20, 684, "{}:{}".format(documento, str(orcamento['cliente']['documento'] or '')))
    pdf.rect(10, 680, 235, 15, fill=False, stroke=True)
    pdf.drawString(250, 684, "Fone:{}".format(listaFones[0]['fone']))
    if len(listaFones) == 2:
        fone2 = listaFones[1]['fone']
    else:
        fone2 = ''
    pdf.rect(245, 680, 200, 15, fill=False, stroke=True)
    pdf.drawString(450, 684, "Fone:{}".format(fone2))
    pdf.rect(445, 680, 140, 15, fill=False, stroke=True)
    pdf.drawString(20, 669, "Endereço:{}".format(str(orcamento['cliente']['endereco'] or ' ')))
    pdf.rect(10, 665, 575, 15, fill=False, stroke=True)
    pdf.drawString(20, 654, "Bairro:{}".format(str(orcamento['cliente']['bairro'] or ' ')))
    pdf.rect(10, 650, 375, 15, fill=False, stroke=True)
    pdf.drawString(390, 654, "CEP:{}".format(str(orcamento['cliente']['cep'] or ' ')))
    pdf.rect(385, 650, 95, 15, fill=False, stroke=True)
    pdf.drawString(485, 654, "Nº:{}".format(str(orcamento['cliente']['numero'] or ' ')))
    pdf.rect(480, 650, 105, 15, fill=False, stroke=True)
    if orcamento['cliente']['cidade'] is None:
        pdf.drawString(20, 639, "Cidade:{}".format(' '))
        pdf.rect(10, 635, 375, 15, fill=False, stroke=True)
        pdf.drawString(390, 639, "UF:{}".format(' '))
        pdf.rect(385, 635, 200, 15, fill=False, stroke=True)
    else:
        pdf.drawString(20, 639, "Cidade:{}".format(orcamento['cliente']['cidade']['nome']))
        pdf.rect(10, 635, 375, 15, fill=False, stroke=True)
        pdf.drawString(390, 639, "UF:{}".format(orcamento['cliente']['cidade']['uf']))
        pdf.rect(385, 635, 200, 15, fill=False, stroke=True)
    pdf.rect(10, 620, 575, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(253, 623, 'Dados do Veículo')
    pdf.setFont('Helvetica', 10)
    pdf.drawString(20, 609, 'Marca:{}'.format(orcamento['veiculo']['marca']['nome']))
    pdf.rect(10, 605, 360, 15, fill=False, stroke=True)
    pdf.drawString(375, 609, 'Ano:{}'.format(str(orcamento['veiculo']['ano'] or ' ')))
    pdf.rect(370, 605, 55, 15, fill=False, stroke=True)
    pdf.drawString(430, 609, 'Placa:')
    pdf.rect(425, 605, 160, 15, fill=False, stroke=True)
    pdf.drawString(20, 594, 'Modelo:{}'.format(orcamento['veiculo']['modelo']))
    pdf.rect(10, 590, 360, 15, fill=False, stroke=True)
    pdf.drawString(375, 594, 'KM:{}'.format(orcamento['km']))
    pdf.rect(370, 590, 215, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    if orcamento['aprovado']:
        pdf.drawString(253, 578, 'Ordem de serviço')
        pdf.setFont('Helvetica', 10)
        pdf.drawString(117, 729, 'Data de Aprovação: {}'.format(orcamento['dataAprovacao'].strftime("%d/%m/%Y")))
        pdf.rect(107, 725, 162, 15, fill=False, stroke=True)
    else:
        pdf.drawString(275, 578, 'Orçamento')
    pdf.rect(10, 575, 575, 15, fill=False, stroke=True)
    # Tabelas de peças e serviços
    pecas = [
        ['Nome da Peça', 'Quantidade', 'Unidade', 'Valor'],
    ]
    servicos = [
        ['Nome do Serviço', 'Quantidade', 'Valor']
    ]
    table_stylepecas = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (3, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_styleservico = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_styleservicopag2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_stylepecaspag2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    # TRANSFORMAR PARA DICIONÁRIO
    if listaPecas:
        for dict in listaPecas:
            pecas.append([dict['descricao'], dict['qtde'], dict['un'], 'R$ {:.2f}'.format(dict['valor'])])

    for dict in listaServicos:
        servicos.append([dict['descricao'], dict['qtde'], 'R$ {:.2f}'.format(dict['valor'])])

    y = 7.9 * inch
    width = 575
    height = 300
    pdf.setFont('Helvetica', 10)

    # Função para posicionar as tabelas de valores e o quadro de observações no pdf.
    # Formatação da primeira página (o máximo de linhas das tabelas que a primeira página pode suportar é 27)
    if len(pecas + servicos) > 27:
        if len(pecas) > 27:
            y = 7.8 * inch
            for _ in range(len(pecas[0:28])):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            y2 = 10.8 * inch
            for _ in range(len(pecas[28:])):
                y2 -= 0.2 * inch
            z2 = y2 - 0.3 * inch
            alturaser = y2 - 0.3 * inch
            for _ in range(len(servicos)):
                alturaser -= 0.2 * inch
            l = alturaser - 0.3 * inch
            g = l - 0.7 * inch
            f = Table(pecas[0:28], colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                      rowHeights=0.2 * inch)
            f2 = Table(pecas[28:], colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                       rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            f.setStyle(table_stylepecas)
            f2.setStyle(table_stylepecaspag2)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f2.wrapOn(pdf, width, height)
            f.drawOn(pdf, 10, y)
            pdf.showPage()
            f2.drawOn(pdf, 10, y2)
            s.drawOn(pdf, 10, alturaser)
            tabelas_pos(pdf, orcamento, l, g)
        else:
            # Caso a tabela peças seja vazia
            if len(pecas) < 2:
                y = 8.3 * inch
                tamanho_ser = 28 - len(pecas)
                z = y - 0.3 * inch
                for _ in range(len(servicos[0:tamanho_ser])):
                    z -= 0.2 * inch
                z2 = z - 0.3 * inch
                alturaser = 10.8 * inch
                for _ in range(len(servicos[tamanho_ser:])):
                    alturaser -= 0.2 * inch
                l = alturaser - 0.3 * inch
                g = l - 0.7 * inch
                s = Table(servicos[0:tamanho_ser], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2 = Table(servicos[tamanho_ser:], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2.setStyle(table_styleservicopag2)
                s.setStyle(table_styleservico)
                s.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                s.drawOn(pdf, 10, z2)
                pdf.showPage()
                s2.drawOn(pdf, 10, alturaser)
                tabelas_pos(pdf, orcamento, l, g)

            else:
                y = 7.8 * inch
                tamanho_ser = 28 - len(pecas)
                for _ in range(len(pecas)):
                    y -= 0.2 * inch
                z = y - 0.3 * inch
                for _ in range(len(servicos[0:tamanho_ser])):
                    z -= 0.2 * inch
                z2 = z + 0.1 * inch
                alturaser = 10.8 * inch
                for _ in range(len(servicos[tamanho_ser:])):
                    alturaser -= 0.2 * inch
                l = alturaser - 0.3 * inch
                g = l - 0.7 * inch
                f = Table(pecas, colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                          rowHeights=0.2 * inch)
                s = Table(servicos[0:tamanho_ser], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2 = Table(servicos[tamanho_ser:], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                f.setStyle(table_stylepecas)
                s.setStyle(table_styleservico)
                s2.setStyle(table_styleservicopag2)
                s.wrapOn(pdf, width, height)
                f.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                # Não deixar o cabeçalho ficar separado da tabela
                if tamanho_ser == 1:
                    f.drawOn(pdf, 10, y)
                    pdf.showPage()
                    s.drawOn(pdf, 10, alturaser)
                    s2.drawOn(pdf, 10, alturaser - 0.2 * inch)
                    l -= 0.4 * inch
                    g -= 0.4 * inch
                else:
                    f.drawOn(pdf, 10, y)
                    s.drawOn(pdf, 10, z2)
                    pdf.showPage()
                    s2.drawOn(pdf, 10, alturaser)

                tabelas_pos(pdf, orcamento, l, g)
    else:
        if len(pecas) < 2:
            y = 7.8 * inch
            for _ in range(len(servicos)):
                y -= 0.2 * inch
            l = y - 0.3 * inch
            g = l - 0.7 * inch
            width = 575
            height = 300
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(pdf, orcamento, l, 70)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            s.drawOn(pdf, 10, y)
        else:
            y = 7.8 * inch
            for _ in range(len(pecas)):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            for _ in range(len(servicos)):
                z -= 0.2 * inch
            l = z - 0.3 * inch
            g = l - 0.7 * inch
            width = 575
            height = 300
            f = Table(pecas, colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(pdf, orcamento, l, 70)
            f.setStyle(table_stylepecas)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f.drawOn(pdf, 10, y)
            s.drawOn(pdf, 10, z)
    pdf.save()
    if path:
        os.startfile(f"{path}\\teste.pdf")
    else:
        os.startfile(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\teste.pdf")

# generatePDF(orcamento, listaFones, listaServicos, listaPecas)
