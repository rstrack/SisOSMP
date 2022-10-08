from sre_constants import _NamedIntConstant
from tkinter import E
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import textwrap
import os
import locale
import phonenumbers

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


# DICT DO ORÇAMENTO GERADO AO SALVAR/EDITAR
# Configurações para geração do pdf
def tabelas_pos(self, orcamento: dict, l, g):
    self.setFont('Helvetica', 10)
    self.drawString(406, l + 4, 'Valor Total')
    self.drawString(541 - (len(str(orcamento['valorTotal'])) * 7.1), l + 4,
                    '{}'.format(locale.currency(orcamento['valorTotal'])))
    self.rect(402, l, 1 * inch + 11, 15, fill=False, stroke=True)
    self.rect(413 + 1 * inch, l, 1 * inch, 15, fill=False, stroke=True)
    self.setFont('Helvetica-Bold', 10)
    self.drawString(44, g + 20, 'Observações:')
    self.setFont('Helvetica', 10)
    linhas = orcamento['observacoes'].split('\n')
    linhasObs = []
    for linha in linhas:
        linhasObs.extend(textwrap.wrap(linha, 115, break_long_words=False))
    c = 123
    q = g + 5
    # pular linha em observações(vai ser melhorado ainda)
    for x in linhasObs:
        self.drawString(44, q, x)
        c = c + 103
        q = q - 15
    self.rect(39, g + 16, 517, 15, fill=False, stroke=True)
    self.rect(39, g - 44, 517, 60, fill=False, stroke=True)


def formatar_cep(self):
    cepformatado = '{}-{}'.format(self[0:5], self[5:])
    return cepformatado


def formatar_fone(self):
    if len(self) > 11:
        print(len(self))
        return (phonenumbers.format_number(phonenumbers.parse("+" + str(self), None),
                                           phonenumbers.PhoneNumberFormat.NATIONAL))
    else:
        return (phonenumbers.format_number(phonenumbers.parse(str(self), 'BR'),
                                           phonenumbers.PhoneNumberFormat.NATIONAL))


def generatePDF(orcamento: dict, listaFones: list[dict], listaServicos: list[dict], listaPecas: list[dict] = None,
                path: str = None):
    if path:
        pdf = canvas.Canvas(f"{path}\\teste.pdf", pagesize=A4)
    else:
        pdf = canvas.Canvas(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\teste.pdf", pagesize=A4)
    pdf.drawInlineImage(
        "./resources/logo2.png", 39, 740, 200, 100
    )
    pdf.setFont('Helvetica-Bold', 10)
    stylesheet = getSampleStyleSheet()
    pdf.normalStyle = stylesheet['Normal']
    tamlinhas = 15
    # Cabeçalho padrão do pdf
    espacamento_subtitulos = 18
    pdf.drawString(312, 814, 'Fone: (42) 3027-4990 / (42) 4141-1755')
    pdf.drawString(260, 798.5, 'Rua Barão do Bojuru, Nº 87 - Ronda - Ponta Grossa - PR')
    pdf.drawString(335, 783, 'CNPJ : 85.481.562/0001-57')
    pdf.drawString(315, 767.5, 'E-mail:mecanicapasetto@gmail.com ')
    pdf.rect(39, 750, 517, 2, fill=True, stroke=True)

    # Informações do Cliente
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(255, 688, 'Dados do Cliente')
    pdf.setFont('Helvetica', 10)
    pdf.drawString(44, 708, 'Data do Orçamento: {}'.format(orcamento['dataOrcamento'].strftime("%d/%m/%Y")))
    pdf.rect(39, 704, 517, 15, fill=False, stroke=True)
    pdf.drawString(44, 668, 'Nome: {}'.format(orcamento['cliente']['nome']))
    pdf.rect(39, 664, 517, 15, fill=False, stroke=True)
    if orcamento['cliente']['tipo'] == '0':
        documento = 'CPF'
        ndoc = str(orcamento['cliente']['documento'])
        cpf = "{}.{}.{}-{}".format(ndoc[0:3], ndoc[3:6], ndoc[6:9], ndoc[9:])
        pdf.drawString(44, 653, "{}: {}".format(documento, cpf or ''))

    elif orcamento['cliente']['tipo'] == '1':
        documento = 'CNPJ'
        ndoc = str(orcamento['cliente']['documento'])
        cnpj = "{}.{}.{}/{}-{}".format(ndoc[0:2], ndoc[2:5], ndoc[5:8], ndoc[8:12], ndoc[12:])
        pdf.drawString(44, 653, "{}: {}".format(documento, cnpj or ''))
    else:
        documento = 'Documento'
        pdf.drawString(44, 653, "{}: {}".format(documento, orcamento['cliente']['documento'] or ''))
    pdf.rect(39, 649, 172.3, 15, fill=False, stroke=True)
    pdf.drawString(216.3, 653, "Fone: {}".format(formatar_fone(listaFones[0]['fone'])))
    if len(listaFones) == 2:
        fone2 = formatar_fone((listaFones[1]['fone']))
    else:
        fone2 = ''
    pdf.rect(211.3, 649, 172.3, 15, fill=False, stroke=True)
    pdf.drawString(388.6, 653, "Fone: {}".format(fone2))
    pdf.rect(383.6, 649, 172.3, 15, fill=False, stroke=True)
    pdf.drawString(44, 638, "Endereço: {}".format(str(orcamento['cliente']['endereco'] or ' ')))
    pdf.rect(39, 634, 441, 15, fill=False, stroke=True)
    pdf.drawString(44, 623, "Bairro: {}".format(str(orcamento['cliente']['bairro'] or ' ')))
    pdf.rect(242, 619, 198, 15, fill=False, stroke=True)
    pdf.drawString(443, 623, "CEP: {}".format(
        (str('{}-{}'.format(orcamento['cliente']['cep'][0:5], orcamento['cliente']['cep'][5:])) or ' ')))
    pdf.rect(440, 619, 80, 15, fill=False, stroke=True)
    pdf.drawString(485, 638, "Nº: {}".format(str(orcamento['cliente']['numero'] or ' ')))
    pdf.rect(480, 634, 76, 15, fill=False, stroke=True)
    if orcamento['cliente']['cidade'] is None:
        pdf.drawString(245, 623, "Cidade:{}".format(' '))
        pdf.rect(39, 619, 203, 15, fill=False, stroke=True)
        pdf.drawString(485, 623, "UF: {}".format(' '))
        pdf.rect(480, 619, 76, 15, fill=False, stroke=True)
    else:
        pdf.drawString(245, 623, "Cidade: {}".format(orcamento['cliente']['cidade']['nome']))
        pdf.rect(39, 619, 203, 15, fill=False, stroke=True)
        pdf.drawString(522, 623, "UF: {}".format(orcamento['cliente']['cidade']['uf']))
        pdf.rect(520, 619, 36, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(253, 603, 'Dados do Veículo')
    pdf.setFont('Helvetica', 10)
    pdf.drawString(44, 583, 'Marca: {}'.format(orcamento['veiculo']['marca']['nome']))
    pdf.rect(39, 579, 331, 15, fill=False, stroke=True)
    pdf.drawString(375, 583, 'Ano: {}'.format(str(orcamento['veiculo']['ano'] or ' ')))
    pdf.rect(370, 579, 55, 15, fill=False, stroke=True)
    pdf.drawString(430, 583, 'Placa: {}'.format(orcamento['veiculo']['placa']))
    pdf.rect(425, 579, 131, 15, fill=False, stroke=True)
    pdf.drawString(44, 568, 'Modelo: {}'.format(orcamento['veiculo']['modelo']))
    pdf.rect(39, 564, 331, 15, fill=False, stroke=True)
    pdf.drawString(375, 568, 'KM: {}'.format(orcamento['km']))
    pdf.rect(370, 564, 186, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    if orcamento['aprovado']:
        pdf.setFont('Helvetica-Bold', 15)
        pdf.drawString(243, 729, 'Ordem de serviço')
        pdf.setFont('Helvetica', 10)
        pdf.drawString(302.5, 708, 'Data de Aprovação: {}'.format(orcamento['dataAprovacao'].strftime("%d/%m/%Y")))
        pdf.rect(297.5, 704, 258.5, 15, fill=False, stroke=True)
    else:
        pdf.setFont('Helvetica-Bold', 15)
        pdf.drawString(263, 729, 'Orçamento')

    # Tabelas de peças e serviços
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(253, 548, 'Peças e Serviços')
    pecas = [
        ['Nome da Peça', 'Unidade', 'Qtde', 'Valor'],
    ]
    servicos = [
        ['Nome do Serviço', 'Qtde', 'Valor']
    ]
    table_stylepecas = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (3, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_styleservico = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_styleservicopag2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    table_stylepecaspag2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])
    # TRANSFORMAR PARA DICIONÁRIO
    if listaPecas:
        for dict in listaPecas:
            pecas.append([dict['descricao'], dict['un'], dict['qtde'], locale.currency(dict['valor'])])

    for dict in listaServicos:
        servicos.append([dict['descricao'], dict['qtde'], locale.currency(dict['valor'])])

    y = 7.5 * inch
    width = 575
    height = 300
    pdf.setFont('Helvetica', 10)

    # Função para posicionar as tabelas de valores e o quadro de observações no pdf.
    # Formatação da primeira página (o máximo de linhas das tabelas que a primeira página pode suportar é 27)
    if len(pecas + servicos) > 26:
        if len(pecas) > 25:
            y = 7.5 * inch
            for _ in range(len(pecas[0:25])):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            y2 = 10.8 * inch
            for _ in range(len(pecas[25:])):
                y2 -= 0.2 * inch
            z2 = y2 - 0.3 * inch
            alturaser = y2 - 0.3 * inch
            for _ in range(len(servicos)):
                alturaser -= 0.2 * inch
            l = alturaser - 0.15 * inch
            g = l - 0.5 * inch
            f = Table(pecas[0:25], colWidths=[4.98 * inch, 0.7 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                      rowHeights=0.2 * inch)
            f2 = Table(pecas[25:], colWidths=[4.98 * inch, 0.7 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                       rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.68 * inch, 0.5 * inch, 1 * inch], rowHeights=0.2 * inch)
            f.setStyle(table_stylepecas)
            f2.setStyle(table_stylepecaspag2)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f2.wrapOn(pdf, width, height)
            f.drawOn(pdf, 39, y)
            pdf.showPage()
            f2.drawOn(pdf, 39, y2)
            s.drawOn(pdf, 39, alturaser)
            tabelas_pos(pdf, orcamento, l, g)
        else:
            # Caso a tabela peças seja vazia
            if len(pecas) < 2:
                y = 8 * inch
                tamanho_ser = 25 - len(pecas)
                z = y - 0.3 * inch
                for _ in range(len(servicos[0:tamanho_ser])):
                    z -= 0.2 * inch
                z2 = z - 0.3 * inch
                alturaser = 10.8 * inch
                for _ in range(len(servicos[tamanho_ser:])):
                    alturaser -= 0.2 * inch
                l = alturaser - 0.3 * inch
                g = l - 0.2 * inch
                s = Table(servicos[0:tamanho_ser], colWidths=[5.68 * inch, 0.5 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2 = Table(servicos[tamanho_ser:], colWidths=[5.68 * inch, 0.5 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2.setStyle(table_styleservicopag2)
                s.setStyle(table_styleservico)
                s.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                s.drawOn(pdf, 39, z2)
                pdf.showPage()
                s2.drawOn(pdf, 39, alturaser)
                tabelas_pos(pdf, orcamento, l, g)

            else:
                y = 7.5 * inch
                tamanho_ser = 25 - len(pecas)
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
                g = l - 0.5 * inch
                f = Table(pecas, colWidths=[4.98 * inch, 0.7 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                          rowHeights=0.2 * inch)
                if tamanho_ser <= 1:
                    s = Table(servicos[tamanho_ser:], colWidths=[5.68 * inch, 0.5 * inch, 1 * inch],
                              rowHeights=0.2 * inch)
                    s.setStyle(table_styleservico)
                    f.setStyle(table_stylepecas)
                    f.wrapOn(pdf, width, height)
                    s.wrapOn(pdf, width, height)
                    f.drawOn(pdf, 39, y)
                    pdf.showPage()
                    s.drawOn(pdf, 39, alturaser)
                    l -= 0.4 * inch
                    g -= 0.4 * inch
                else:
                    s = Table(servicos[0:tamanho_ser], colWidths=[5.68 * inch, 0.5 * inch, 1 * inch],
                              rowHeights=0.2 * inch)
                    s2 = Table(servicos[tamanho_ser:], colWidths=[5.68 * inch, 0.5 * inch, 1 * inch],
                               rowHeights=0.2 * inch)
                    s.setStyle(table_styleservico)
                    s2.setStyle(table_styleservicopag2)
                    f.setStyle(table_stylepecas)
                    f.wrapOn(pdf, width, height)
                    s.wrapOn(pdf, width, height)
                    s2.wrapOn(pdf, width, height)
                    f.drawOn(pdf, 39, y)
                    s.drawOn(pdf, 39, z2)
                    pdf.showPage()
                    s2.drawOn(pdf, 39, alturaser)
                # Não deixar o cabeçalho ficar separado da tabela
                tabelas_pos(pdf, orcamento, l, g)
    else:
        if len(pecas) < 2:
            y = 7.5 * inch
            for _ in range(len(servicos)):
                y -= 0.2 * inch
            l = y - 0.3 * inch
            g = l - 0.5 * inch
            width = 575
            height = 300
            s = Table(servicos, colWidths=[5.68 * inch, 0.5 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(pdf, orcamento, l, 70)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            s.drawOn(pdf, 40, y)
        else:
            y = 7.5 * inch
            for _ in range(len(pecas)):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            for _ in range(len(servicos)):
                z -= 0.2 * inch
            l = z - 0.3 * inch
            g = l - 0.7 * inch
            width = 575
            height = 300
            f = Table(pecas, colWidths=[4.98 * inch, 0.7 * inch, 0.5 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.68 * inch, 0.5 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(pdf, orcamento, l, 70)
            f.setStyle(table_stylepecas)
            s.setStyle(table_styleservico)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f.drawOn(pdf, 39, y)
            s.drawOn(pdf, 39, z)
    pdf.save()
    if path:
        os.startfile(f"{path}\\teste.pdf")
    else:
        os.startfile(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\teste.pdf")

# generatePDF(orcamento, listaFones, listaServicos, listaPecas)
