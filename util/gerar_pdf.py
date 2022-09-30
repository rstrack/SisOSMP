from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
import os

lista1 = [['Daniel Pasetto', 'CNPJ', '85.481.562/0001-57', "12345678910", "12345678910", "Rua Barão do Bojuru", "Ronda",
           "84070-310", "87", "Ponta Grossa", "PR", "Volkswagen", "9999", "Saveiro-Kombi", "999999"],
          [['Carburador', '5', 'Unidade', 'R$ 50.00'], ['Pneu', '3', 'Unidade', 'R$ 50.00']],
          [['Troca de Peça', '5', 'R$ 50.00']]]


# Configurações para geração do pdf


def GeneratePDF(listainfos):
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
    pdf.rect(10, 710, 575, 15, fill=False, stroke=True)
    pdf.drawString(20, 699, 'Nome:{}'.format(listainfos[0][0]))
    pdf.rect(10, 695, 575, 15, fill=False, stroke=True)
    pdf.drawString(20, 684, "{}:{}".format(listainfos[0][1], listainfos[0][2]))
    pdf.rect(10, 680, 235, 15, fill=False, stroke=True)
    pdf.drawString(250, 684, "Fone:{}".format(listainfos[0][3]))
    pdf.rect(245, 680, 200, 15, fill=False, stroke=True)
    pdf.drawString(450, 684, "Fone:{}".format(listainfos[0][4]))
    pdf.rect(445, 680, 140, 15, fill=False, stroke=True)
    pdf.drawString(20, 669, "Endereço:{}".format(listainfos[0][5]))
    pdf.rect(10, 665, 575, 15, fill=False, stroke=True)
    pdf.drawString(20, 654, "Bairro:{}".format(listainfos[0][6]))
    pdf.rect(10, 650, 375, 15, fill=False, stroke=True)
    pdf.drawString(390, 654, "CEP:{}".format(listainfos[0][7]))
    pdf.rect(385, 650, 95, 15, fill=False, stroke=True)
    pdf.drawString(485, 654, "Nº:{}".format(listainfos[0][8]))
    pdf.rect(480, 650, 105, 15, fill=False, stroke=True)
    pdf.drawString(20, 639, "Cidade:{}".format(listainfos[0][9]))
    pdf.rect(10, 635, 375, 15, fill=False, stroke=True)
    pdf.drawString(390, 639, "UF:{}".format(listainfos[0][10]))
    pdf.rect(385, 635, 200, 15, fill=False, stroke=True)
    pdf.rect(10, 620, 575, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(253, 623, 'Dados do Veículo')
    pdf.setFont('Helvetica', 10)
    pdf.drawString(20, 609, 'Marca:{}'.format(listainfos[0][11]))
    pdf.rect(10, 605, 360, 15, fill=False, stroke=True)
    pdf.drawString(375, 609, 'Ano:{}'.format(listainfos[0][12]))
    pdf.rect(370, 605, 55, 15, fill=False, stroke=True)
    pdf.drawString(430, 609, 'Placa:')
    pdf.rect(425, 605, 160, 15, fill=False, stroke=True)
    pdf.drawString(20, 594, 'Modelo:{}'.format(listainfos[0][13]))
    pdf.rect(10, 590, 360, 15, fill=False, stroke=True)
    pdf.drawString(375, 594, 'KM:{}'.format(listainfos[0][14]))
    pdf.rect(370, 590, 215, 15, fill=False, stroke=True)
    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(275, 578, 'Orçamento')
    pdf.rect(10, 575, 575, 15, fill=False, stroke=True)
    # Tabelas de peças e serviços
    pecas = [
        ['Nome da Peça', 'Quantidade', 'Unidade', 'Valor'],
    ]
    servicos = [
        ['Nome do Serviço', 'Quantidade', 'Valor']
    ]
    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])

    pecasitem = 0
    num_elementos_listapecas = len(listainfos[1])
    while pecasitem < num_elementos_listapecas:
        pecas.append(listainfos[1][pecasitem])
        pecasitem += 1
    servicositem = 0
    num_elementos_listaservicos = len(listainfos[2])
    while servicositem < num_elementos_listaservicos:
        servicos.append(listainfos[2][servicositem])
        servicositem += 1

    y = 7.9 * inch
    print(len(pecas + servicos))
    width = 575
    height = 300
    pdf.setFont('Helvetica', 10)

    # Função para posicionar as tabelas de valores e o quadro de observações no pdf.

    def tabelas_pos(l, g):
        pdf.setFont('Helvetica', 10)
        pdf.drawString(395, l + 4, 'Valor Total das Peças:')
        pdf.rect(390, l, 1 * inch + 51, 15, fill=False, stroke=True)
        pdf.rect(441 + 1 * inch, l, 1 * inch, 15, fill=False, stroke=True)
        pdf.drawString(395, l - 11, 'Valor Total dos Serviços:')
        pdf.rect(390, l - 15, 1 * inch + 51, 15, fill=False, stroke=True)
        pdf.rect(441 + 1 * inch, l - 15, 1 * inch, 15, fill=False, stroke=True)
        pdf.drawString(395, l - 26, 'Valor Total:')
        pdf.rect(390, l - 30, 1 * inch + 51, 15, fill=False, stroke=True)
        pdf.rect(441 + 1 * inch, l - 30, 1 * inch, 15, fill=False, stroke=True)
        pdf.drawString(265, g + 4, 'Observações:')
        obs = "O Carro mostrou avarias na parte traseira, foi encontrado um cavalo no interior do veículo cujo o " \
              "mesmo foi agressivo com o mecanico.kjadsaksjdsj kjdkasjdkjdsakjadsjkads "
        aux = 0
        c = 123
        q = g - 11
        # pular linha em observações(vai ser melhorado ainda)
        for x in range(5):
            pdf.drawString(30, q, obs[aux:c])
            aux = c + 1
            c = c + 103
            q = q - 15
        pdf.rect(10, g, 575, 15, fill=False, stroke=True)
        pdf.rect(10, g - 60, 575, 60, fill=False, stroke=True)

    # Formatação da primeira página (o máximo de linhas das tabelas que a primeira página pode suportar é 27)
    if len(pecas + servicos) >= 28:
        if len(pecas) >= 28:
            y = 7.9 * inch
            for x in range(len(pecas[0:28])):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            y2 = 10.8 * inch
            for x2 in range(len(pecas[28:])):
                y2 -= 0.2 * inch
            z2 = y2 - 0.3 * inch
            alturaser = y2 - 0.3 * inch
            for k in range(len(servicos)):
                alturaser -= 0.2 * inch
            l = alturaser - 0.3 * inch
            g = l - 0.7 * inch
            print(len(pecas + servicos))
            f = Table(pecas[0:28], colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                      rowHeights=0.2 * inch)
            f2 = Table(pecas[28:], colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                       rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            f.setStyle(table_style)
            f2.setStyle(table_style)
            s.setStyle(table_style)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f2.wrapOn(pdf, width, height)
            f.drawOn(pdf, 10, y)
            pdf.showPage()
            f2.drawOn(pdf, 10, y2)
            s.drawOn(pdf, 10, alturaser)
            tabelas_pos(l, g)
        else:
            # Caso a tabela peças seja vazia
            if len(pecas) < 2:
                y = 8.3 * inch
                tamanho_ser = 28 - len(pecas)
                z = y - 0.3 * inch
                for x2 in range(len(servicos[0:tamanho_ser])):
                    z -= 0.2 * inch
                z2 = z - 0.3 * inch
                alturaser = 10.8 * inch
                for k in range(len(servicos[tamanho_ser:])):
                    alturaser -= 0.2 * inch
                l = alturaser - 0.3 * inch
                g = l - 0.7 * inch
                print(len(pecas + servicos))
                s = Table(servicos[0:tamanho_ser], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2 = Table(servicos[tamanho_ser:], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2.setStyle(table_style)
                s.setStyle(table_style)
                s.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                s.drawOn(pdf, 10, z2)
                pdf.showPage()
                s2.drawOn(pdf, 10, alturaser)
                tabelas_pos(l, g)
            else:
                y = 7.9 * inch
                tamanho_ser = 28 - len(pecas)
                for x in range(len(pecas)):
                    y -= 0.2 * inch
                z = y - 0.3 * inch
                for x2 in range(len(servicos[0:tamanho_ser])):
                    z -= 0.2 * inch
                z2 = z - 0.3 * inch
                alturaser = 10.8 * inch
                for k in range(len(servicos[tamanho_ser:])):
                    alturaser -= 0.2 * inch
                l = alturaser - 0.3 * inch
                g = l - 0.7 * inch
                print(len(pecas + servicos))
                f = Table(pecas, colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch],
                          rowHeights=0.2 * inch)
                s = Table(servicos[0:tamanho_ser], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                s2 = Table(servicos[tamanho_ser:], colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
                f.setStyle(table_style)
                s2.setStyle(table_style)
                s.setStyle(table_style)
                s.wrapOn(pdf, width, height)
                f.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                f.drawOn(pdf, 10, y)
                s.drawOn(pdf, 10, z2)
                pdf.showPage()
                s2.drawOn(pdf, 10, alturaser)
                tabelas_pos(l, g)
    else:
        if len(pecas) < 2:
            y = 7.9 * inch
            for k in range(len(servicos)):
                y -= 0.2 * inch
            l = y - 0.3 * inch
            g = l - 0.7 * inch
            print(len(pecas + servicos))
            width = 575
            height = 300
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(l, g)
            s.setStyle(table_style)
            s.wrapOn(pdf, width, height)
            s.drawOn(pdf, 10, y)
        else:
            y = 7.9 * inch
            for x in range(len(pecas)):
                y -= 0.2 * inch
            z = y - 0.3 * inch
            for k in range(len(servicos)):
                z -= 0.2 * inch
            l = z - 0.3 * inch
            g = l - 0.7 * inch
            print(len(pecas + servicos))
            width = 575
            height = 300
            f = Table(pecas, colWidths=[4.98 * inch, 1 * inch, 1 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            s = Table(servicos, colWidths=[5.98 * inch, 1 * inch, 1 * inch], rowHeights=0.2 * inch)
            tabelas_pos(l, g)
            f.setStyle(table_style)
            s.setStyle(table_style)
            s.wrapOn(pdf, width, height)
            f.wrapOn(pdf, width, height)
            f.drawOn(pdf, 10, y)
            s.drawOn(pdf, 10, z)
    pdf.save()
    os.startfile(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\teste.pdf")
    print('teste.pdf criado com sucesso!')


GeneratePDF(lista1)
