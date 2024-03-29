import locale
import os
import re
import phonenumbers
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER


class GeraPDF:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    def draw_paragraph(self, pdf, msg, x, y, max_width, max_height):
        msg = msg.replace("\n", " ")
        message_style = ParagraphStyle(
            "Estilo do paragrafo de observacao",
            fontName="Helvetica",
            splitLongWords=False,
        )
        message = msg.replace("\n", "<br />")
        message = Paragraph(message, style=message_style)
        _, h = message.wrap(max_width, max_height)
        message.drawOn(pdf, x, y - h)

    # DICT DO ORÇAMENTO GERADO AO SALVAR/EDITAR
    # Configurações para geração do pdf
    def tabelas_pos(self, pdf, orcamento: dict, l, g, somapeca, somaservicos):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(410, l + 4, "Total Peças")
        pdf.drawString(410, l - 11, "Total Serviços")
        pdf.drawString(410, l - 26, "Valor Total")
        pdf.setFont("Helvetica", 10)
        pdf.drawRightString(550, l - 26, str(locale.currency(orcamento["valorTotal"])))
        pdf.drawRightString(550, l + 4, str(locale.currency(somapeca)))
        pdf.drawRightString(550, l - 11, str(locale.currency(somaservicos)))
        pdf.rect(407, l, 77, 15, fill=False, stroke=True)
        pdf.rect(484, l, 1 * inch, 15, fill=False, stroke=True)
        pdf.rect(407, l - 15, 77, 15, fill=False, stroke=True)
        pdf.rect(484, l - 15, 1 * inch, 15, fill=False, stroke=True)
        pdf.rect(407, l - 30, 77, 15, fill=False, stroke=True)
        pdf.rect(484, l - 30, 1 * inch, 15, fill=False, stroke=True)
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(44, g + 20, "Observações:")
        pdf.setFont("Helvetica", 10)
        c = 123
        q = g + 15
        self.draw_paragraph(pdf, str((orcamento["observacoes"]) or ""), 44, q, 510, 55)
        # pular linha em observações(vai ser melhorado ainda)
        pdf.rect(39, g + 16, 517, 15, fill=False, stroke=True)
        pdf.rect(39, g - 44, 517, 60, fill=False, stroke=True)

    def formatar_cep(self, cep):
        if cep:
            cepformatado = f"{cep[0:5]}-{cep[5:]}"
            return cepformatado
        return str(" ")

    def formatar_placa(self, placa):
        if placa:
            placaformatada = f"{placa[0:3]}-{placa[3:]}"
            return placaformatada
        return str(" ")

    def paginacao(self, pdf, cont):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawRightString(570, 10, f" Página {pdf.getPageNumber()} de {cont}")
        pdf.setFont("Helvetica", 10)

    def formatar_fone(self, fone):
        try:
            if len(fone) > 11:
                return phonenumbers.format_number(
                    phonenumbers.parse("+" + str(fone), None),
                    phonenumbers.PhoneNumberFormat.NATIONAL,
                )
            return phonenumbers.format_number(
                phonenumbers.parse(str(fone), "BR"),
                phonenumbers.PhoneNumberFormat.NATIONAL,
            )
        except:
            return fone

    def generatePDF(
            self,
            orcamento: dict,
            listaFones: list[dict],
            listaServicos: list[dict],
            listaPecas: list[dict] = None,
            path: str = None,
    ):
        nomearquivo = f"{orcamento['veiculo']['modelo']} {orcamento['veiculo']['placa']} ({orcamento['cliente']['nome']}) {orcamento['dataOrcamento'].strftime('%d-%m-%Y')}.pdf"
        nomearquivo = (
            nomearquivo.replace("/", "-")
                .replace("#", "")
                .replace("<", "")
                .replace(">", "")
                .replace("!", "")
                .replace("$", "")
                .replace("+", "")
                .replace("*", "")
                .replace("{", "")
                .replace("}", "")
                .replace("|", "")
                .replace("@", "")
        )
        if path:
            pdf = canvas.Canvas(f"{path}\\{nomearquivo}", pagesize=A4)
        else:
            pdf = canvas.Canvas(
                f"{os.path.expandvars('%LOCALAPPDATA%')}\\Temp\\{nomearquivo}",
                pagesize=A4,
            )
        pdf.drawInlineImage("resources/logo2.png", 39, 740, 200, 100)
        pdf.setFont("Helvetica-Bold", 10)
        stylesheet = getSampleStyleSheet()
        pdf.normalStyle = stylesheet["Normal"]
        # Cabeçalho padrão do pdf
        pdf.drawString(312, 814, "Fone: (42) 3027-4990 / (42) 4141-1755")
        pdf.drawString(
            260, 798.5, "Rua Barão do Bojuru, Nº 87 - Ronda - Ponta Grossa - PR"
        )
        pdf.drawString(335, 783, "CNPJ : 85.481.562/0001-57")
        pdf.drawString(315, 767.5, "E-mail:mecanicapasetto@gmail.com ")
        pdf.rect(39, 750, 517, 2, fill=True, stroke=True)
        # Informações do Cliente
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(255, 688, "Dados do Cliente")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(
            44,
            708,
            f'Data do Orçamento: {orcamento["dataOrcamento"].strftime("%d/%m/%Y")}',
        )
        pdf.rect(39, 704, 517, 15, fill=False, stroke=True)
        pdf.drawString(44, 668, f'Nome: {orcamento["cliente"]["nome"]}')
        pdf.rect(39, 664, 517, 15, fill=False, stroke=True)
        if orcamento["cliente"]["documento"] is not None:
            if orcamento["cliente"]["tipo"] == "0":
                documento = "CPF"
                ndoc = str(orcamento["cliente"]["documento"])
                cpf = f"{ndoc[0:3]}.{ndoc[3:6]}.{ndoc[6:9]}-{ndoc[9:]}"
                pdf.drawString(44, 653, f"{documento}: {cpf or ''}")
            elif orcamento["cliente"]["tipo"] == "1":
                documento = "CNPJ"
                ndoc = str(orcamento["cliente"]["documento"])
                cnpj = f"{ndoc[0:2]}.{ndoc[2:5]}.{ndoc[5:8]}/{ndoc[8:12]}-{ndoc[12:]}"
                pdf.drawString(44, 653, f"{documento}: {cnpj or ''}")
            else:
                documento = "Documento"
                pdf.drawString(
                    44, 653, f"{documento}: {orcamento['cliente']['documento'] or ''}"
                )
        else:
            pdf.drawString(44, 653, "Documento:")
        pdf.rect(39, 649, 172.3, 15, fill=False, stroke=True)
        pdf.drawString(216.3, 653, f"Fone: {self.formatar_fone(listaFones[0]['fone'])}")
        if len(listaFones) == 2:
            fone2 = self.formatar_fone((listaFones[1]["fone"]))
        else:
            fone2 = ""
        pdf.rect(211.3, 649, 172.3, 15, fill=False, stroke=True)
        pdf.drawString(388.6, 653, f"Fone: {fone2}")
        pdf.rect(383.6, 649, 172.3, 15, fill=False, stroke=True)
        pdf.drawString(
            44, 638, f"Endereço: {str(orcamento['cliente']['endereco']) or ''}"
        )
        pdf.rect(39, 634, 441, 15, fill=False, stroke=True)
        pdf.drawString(44, 623, "Bairro:")
        if orcamento["cliente"]["bairro"]:
            if len(orcamento["cliente"]["bairro"]) < 25:
                pdf.drawString(74, 623, f"{str(orcamento['cliente']['bairro'] or ' ')}")
            elif len(orcamento["cliente"]["bairro"]) < 35:
                pdf.setFont("Helvetica", 8)
                pdf.drawString(74, 624, f"{str(orcamento['cliente']['bairro'] or ' ')}")
                pdf.setFont("Helvetica", 10)
            else:
                pdf.setFont("Helvetica", 5)
                pdf.drawString(
                    74, 624, "{}".format(str(orcamento["cliente"]["bairro"] or " "))
                )
                pdf.setFont("Helvetica", 10)

        pdf.rect(242, 619, 198, 15, fill=False, stroke=True)
        pdf.drawString(
            443,
            623,
            "CEP: {}".format(self.formatar_cep(orcamento["cliente"]["cep"])) or " ",
        )
        pdf.rect(440, 619, 80, 15, fill=False, stroke=True)
        pdf.drawString(
            485, 638, "Nº: {}".format(str(orcamento["cliente"]["numero"] or " "))
        )
        pdf.rect(480, 634, 76, 15, fill=False, stroke=True)
        if orcamento["cliente"]["cidade"] is None:
            pdf.drawString(245, 623, "Cidade: ")
            pdf.rect(39, 619, 203, 15, fill=False, stroke=True)
            pdf.drawString(523, 623, "UF:")
            pdf.rect(520, 619, 36, 15, fill=False, stroke=True)
        else:
            pdf.drawString(
                245, 623, "Cidade: {}".format(orcamento["cliente"]["cidade"]["nome"])
            )
            pdf.rect(39, 619, 203, 15, fill=False, stroke=True)
            pdf.drawString(
                523, 623, "UF:{}".format(orcamento["cliente"]["cidade"]["uf"])
            )
            pdf.rect(520, 619, 36, 15, fill=False, stroke=True)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(253, 603, "Dados do Veículo")
        pdf.setFont("Helvetica", 10)
        pdf.drawString(
            44, 583, "Marca: {}".format(orcamento["veiculo"]["marca"]["nome"])
        )
        pdf.rect(39, 579, 331, 15, fill=False, stroke=True)
        pdf.drawString(
            375, 583, "Ano: {}".format(str(orcamento["veiculo"]["ano"] or " "))
        )
        pdf.rect(370, 579, 55, 15, fill=False, stroke=True)
        if re.match("([A-Za-z]{3}[0-9]{4})", orcamento["veiculo"]["placa"]):
            pdf.drawString(430, 583, "Placa: {}".format(self.formatar_placa(orcamento["veiculo"]["placa"])) or " ", )
        else:
            pdf.drawString(430, 583, "Placa: {}".format(orcamento["veiculo"]["placa"]))
        pdf.rect(425, 579, 131, 15, fill=False, stroke=True)
        pdf.drawString(44, 568, "Modelo: {}".format(orcamento["veiculo"]["modelo"]))
        pdf.rect(39, 564, 331, 15, fill=False, stroke=True)
        pdf.drawString(375, 568, "KM: {}".format(orcamento["km"]))
        pdf.rect(370, 564, 186, 15, fill=False, stroke=True)
        pdf.setFont("Helvetica-Bold", 12)
        if orcamento["status"] in ["2", "3"]:
            pdf.setFont("Helvetica-Bold", 15)
            pdf.drawString(243, 729, "Ordem de serviço")
            pdf.setFont("Helvetica", 10)
            pdf.drawString(
                302.5,
                708,
                "Data de Aprovação: {}".format(
                    orcamento["dataAprovacao"].strftime("%d/%m/%Y")
                ),
            )
            pdf.rect(297.5, 704, 258.5, 15, fill=False, stroke=True)
        else:
            pdf.setFont("Helvetica-Bold", 15)
            pdf.drawString(263, 729, "Orçamento")
            pdf.setFont("Helvetica-Bold", 7)
            pdf.drawString(44, 697, "*Orçamento sujeito a alteração.")

        # Tabelas de peças e serviços
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(253, 548, "Peças e Serviços")
        pecas = [
            ["Peças", "Qtde", "UN", "Valor UN", "Valor Total"],
        ]
        servicos = [["Serviços", "Valor Total"]]

        table_stylepecas = TableStyle(
            [
                ("FONTNAME", (0, 0), (5, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 1), (1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (2, 0), (-1, -1), "LEFT"),
                ("ALIGN", (3, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (4, 0), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
        table_styleservico = TableStyle(
            [
                ("FONTNAME", (0, 0), (4, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 1), (1, -1), 9),
                ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
        table_styleservicopag2 = TableStyle(
            [
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (2, 0), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
        table_stylepecaspag2 = TableStyle(
            [
                ("FONTSIZE", (0, 1), (1, -1), 9),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (2, 0), (-1, -1), "LEFT"),
                ("ALIGN", (3, 0), (-1, -1), "RIGHT"),
                ("ALIGN", (4, 0), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("INNERGRID", (0, 0), (-1, -1), 1, colors.black),
                ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ]
        )

        # TRANSFORMAR PARA DICIONÁRIO
        if listaPecas:
            for dict in listaPecas:
                dict["valortot"] = float(dict["valor"] * dict["qtde"])
                pecas.append(
                    [
                        dict["descricao"],
                        round(dict["qtde"])
                        if float(dict["qtde"]).is_integer()
                        else dict["qtde"],
                        dict["un"],
                        locale.currency(dict["valor"]),
                        locale.currency(dict["valortot"]),
                    ]
                )
        somapeca = 0
        for valor in pecas[1:]:
            valorbruto = valor[4].replace('R$ ', "")
            valorbruto = valorbruto.replace(',', '.')
            somapeca += float(valorbruto)

        for dict in listaServicos:
            servicos.append(
                [dict["descricao"], locale.currency(dict["valor"])]
            )
        somaservicos = 0
        for valor in servicos[1:]:
            valorbruto = valor[1].replace('R$ ', "")
            valorbruto = valorbruto.replace(',', '.')
            somaservicos += float(valorbruto)

        y = 7.5 * inch
        width = 575
        height = 300
        countpage = 1
        n = 0
        style = getSampleStyleSheet()
        styleN = style["BodyText"]
        styleN.alignment = TA_LEFT
        styleN.wordWrap = 'CJK'
        incre1 = 0
        incre2 = 0
        incre3 = 0
        increaux = 0
        impar = False
        j = 0
        k = 0
        aux = len(pecas)
        pecasduaslinhas = []
        for n in range(len(pecas)):
            attlen = len(pecas[n][0])
            if len(pecas[n][0]) >= 50:
                pecasduaslinhas.append(n)
                increaux += 1
        for u, valoru in enumerate(pecasduaslinhas):
            valorindice = u + valoru
            pecas[valorindice][0] = [Paragraph(pecas[valorindice][0], styleN)]
            pecas.insert(u + valoru + 1, [{}])
        for j in range(len(pecas)):
            if j <= 23:
                if pecas[j][0] == {}:
                    table_stylepecas.add("SPAN", (0, j - 1), (0, j))
                    table_stylepecas.add("SPAN", (1, j - 1), (1, j))
                    table_stylepecas.add("SPAN", (2, j - 1), (2, j))
                    table_stylepecas.add("SPAN", (3, j - 1), (3, j))
                    table_stylepecas.add("SPAN", (4, j - 1), (4, j))
            else:
                if len(pecas[j][0]) >= 50:
                    pecas[j][0] = [Paragraph(pecas[j][0], styleN)]
                    pecas.insert(j + 1, [{}])
                    table_stylepecaspag2.add("FONTSIZE", (0, 1), (1, -1), 9)
                    table_stylepecaspag2.add('SPAN', (0, j - 24), (0, j - 23))
                    table_stylepecaspag2.add('SPAN', (1, j - 24), (1, j - 23))
                    table_stylepecaspag2.add('SPAN', (2, j - 24), (2, j - 23))
                    table_stylepecaspag2.add("SPAN", (3, j - 24), (3, j - 23))
                    table_stylepecaspag2.add("SPAN", (4, j - 24), (4, j - 23))
        # Função para posicionar as tabelas de valores e o quadro de observações no pdf.
        # Formatação da primeira página (o máximo de linhas das tabelas que a primeira página pode suportar é 27)
        if len(pecas + servicos) >= 26:
            if len(pecas) >= 24:
                print(pecas[23][0] is not {} and type(pecas[23][0]) is list)
                if pecas[23][0] is not {} and type(pecas[23][0]) is list:
                    for j in range(len(pecas)):
                        if j <= 24:
                            if pecas[j][0] == {}:
                                table_stylepecas.add("SPAN", (0, j - 1), (0, j))
                                table_stylepecas.add("SPAN", (1, j - 1), (1, j))
                                table_stylepecas.add("SPAN", (2, j - 1), (2, j))
                                table_stylepecas.add("SPAN", (3, j - 1), (3, j))
                                table_stylepecas.add("SPAN", (4, j - 1), (4, j))
                                incre1 += 1
                        else:
                            if type(pecas[j][0]) is list:
                                table_stylepecaspag2.add("FONTSIZE", (0, 1), (1, -1), 9)
                                table_stylepecaspag2.add('SPAN', (0, j - 25), (0, j - 24))
                                table_stylepecaspag2.add('SPAN', (1, j - 25), (1, j - 24))
                                table_stylepecaspag2.add('SPAN', (2, j - 25), (2, j - 24))
                                table_stylepecaspag2.add("SPAN", (3, j - 25), (3, j - 24))
                                table_stylepecaspag2.add("SPAN", (4, j - 25), (4, j - 24))
                                incre2 += 2
                    f = Table(
                        pecas[0:25],
                        colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                        rowHeights=0.2 * inch,
                    )
                    if len(pecas) != 25:
                        f2 = Table(
                            pecas[25:],
                            colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                            rowHeights=0.2 * inch,
                        )
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
                        l = alturaser - 0.3 * inch
                    g = l - 1 * inch
                else:
                    for k in range(len(pecas)):
                        if k <= 25:
                            if pecas[k][0] == {}:
                                table_stylepecas.add("SPAN", (0, k - 1), (0, k))
                                table_stylepecas.add("SPAN", (1, k - 1), (1, k))
                                table_stylepecas.add("SPAN", (2, k - 1), (2, k))
                                table_stylepecas.add("SPAN", (3, k - 1), (3, k))
                                table_stylepecas.add("SPAN", (4, k - 1), (4, k))
                                incre1 += 1
                        else:
                            if type(pecas[k][0]) is list:
                                table_stylepecaspag2.add("FONTSIZE", (0, 1), (1, -1), 9)
                                table_stylepecaspag2.add('SPAN', (0, k - 25), (0, k - 24))
                                table_stylepecaspag2.add('SPAN', (1, k - 25), (1, k - 24))
                                table_stylepecaspag2.add('SPAN', (2, k - 25), (2, k - 24))
                                table_stylepecaspag2.add("SPAN", (3, k - 25), (3, k - 24))
                                table_stylepecaspag2.add("SPAN", (4, k - 25), (4, k - 24))
                                incre2 += 1
                    f = Table(
                        pecas[0:25],
                        colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                        rowHeights=0.2 * inch,
                    )
                    if len(pecas) != 25:
                        f2 = Table(
                            pecas[25:],
                            colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                            rowHeights=0.2 * inch,
                        )
                    y = 7.5 * inch
                    if len(pecas) != 25:
                        for _ in range(len(pecas[0:24])):
                            y -= 0.2 * inch
                    else:
                        for _ in range(len(pecas[0:25])):
                            y -= 0.2 * inch
                    z = y - 0.3 * inch
                    y2 = 10.8 * inch
                    for _ in range(len(pecas[24:])):
                        y2 -= 0.2 * inch
                    z2 = y2 - 0.3 * inch
                    alturaser = y2 - 0.3 * inch
                    for _ in range(len(servicos)):
                        alturaser -= 0.2 * inch
                    if len(pecas) <= 25:
                        l = alturaser - 0.3 * inch
                        print(l)
                    else:
                        l = (alturaser - 0.3 * inch) - (incre2 * 0.3 * inch)
                        print(l)
                    g = l - 1 * inch
                s2 = Table(
                    servicos,
                    colWidths=[6.18 * inch, 1 * inch],
                    rowHeights=0.2 * inch,
                )
                f.setStyle(table_stylepecas)
                if len(pecas) != 25:
                    f2.setStyle(table_stylepecaspag2)
                s2.setStyle(table_styleservico)
                f.wrapOn(pdf, width, height)
                if len(pecas) != 25:
                    f2.wrapOn(pdf, width, height)
                s2.wrapOn(pdf, width, height)
                f.drawOn(pdf, 39, y)
                self.paginacao(pdf, (countpage + 1))
                pdf.showPage()
                self.paginacao(pdf, (countpage + 1))
                if len(pecas) != 25:
                    f2.drawOn(pdf, 39, y2)
                s2.drawOn(pdf, 39, alturaser)
                self.tabelas_pos(pdf, orcamento, l, g, somapeca, somaservicos)
            else:
                # Caso a tabela peças seja vazia
                if len(pecas) < 2:
                    y = 8 * inch
                    tamanho_ser = 24 - len(pecas)
                    z = y - 0.3 * inch
                    for _ in range(len(servicos[0:tamanho_ser])):
                        z -= 0.2 * inch
                    z2 = z - 0.3 * inch
                    alturaser = 10.8 * inch
                    for _ in range(len(servicos[tamanho_ser:])):
                        alturaser -= 0.2 * inch
                    l = alturaser - 0.3 * inch
                    g = l - (1 * inch)
                    s = Table(
                        servicos[0:tamanho_ser],
                        colWidths=[6.18 * inch, 1 * inch],
                        rowHeights=0.2 * inch,
                    )
                    s2 = Table(
                        servicos[tamanho_ser:],
                        colWidths=[6.18 * inch, 1 * inch],
                        rowHeights=0.2 * inch,
                    )
                    s2.setStyle(table_styleservicopag2)
                    s.setStyle(table_styleservico)
                    s.wrapOn(pdf, width, height)
                    s2.wrapOn(pdf, width, height)
                    s.drawOn(pdf, 39, z2)
                    self.paginacao(pdf, (countpage + 1))
                    pdf.showPage()
                    self.paginacao(pdf, (countpage + 1))
                    s2.drawOn(pdf, 39, alturaser)
                    self.tabelas_pos(pdf, orcamento, l, g, somapeca, somaservicos)

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
                    g = l - 1 * inch
                    f = Table(
                        pecas,
                        colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                        rowHeights=0.2 * inch,
                    )
                    if tamanho_ser == 1:
                        s = Table(
                            servicos,
                            colWidths=[6.18 * inch, 1 * inch],
                            rowHeights=0.2 * inch,
                        )
                        s.setStyle(table_styleservico)
                        f.setStyle(table_stylepecas)
                        f.wrapOn(pdf, width, height)
                        s.wrapOn(pdf, width, height)
                        f.drawOn(pdf, 39, y)
                        self.paginacao(pdf, (countpage + 1))
                        pdf.showPage()
                        self.paginacao(pdf, (countpage + 1))
                        s.drawOn(pdf, 39, alturaser)
                        l -= 0.4 * inch
                        g -= 0.4 * inch

                    else:
                        s = Table(
                            servicos[0:tamanho_ser],
                            colWidths=[6.18 * inch, 1 * inch],
                            rowHeights=0.2 * inch,
                        )
                        s2 = Table(
                            servicos[tamanho_ser:],
                            colWidths=[6.18 * inch, 1 * inch],
                            rowHeights=0.2 * inch,
                        )
                        s.setStyle(table_styleservico)
                        s2.setStyle(table_styleservicopag2)
                        f.setStyle(table_stylepecas)
                        f.wrapOn(pdf, width, height)
                        s.wrapOn(pdf, width, height)
                        s2.wrapOn(pdf, width, height)
                        f.drawOn(pdf, 39, y)
                        s.drawOn(pdf, 39, z2)
                        self.paginacao(pdf, (countpage + 1))
                        pdf.showPage()
                        self.paginacao(pdf, (countpage + 1))
                        s2.drawOn(pdf, 39, alturaser)
                    # Não deixar o cabeçalho ficar separado da tabela
                    self.tabelas_pos(pdf, orcamento, l, g, somapeca, somaservicos)
        else:
            if len(pecas) < 2:
                y = 7.5 * inch
                for _ in range(len(servicos)):
                    y -= 0.2 * inch
                l = y - 0.3 * inch
                g = l - 0.5 * inch
                width = 575
                height = 300
                s = Table(
                    servicos,
                    colWidths=[6.18 * inch, 1 * inch],
                    rowHeights=0.2 * inch,
                )
                self.tabelas_pos(pdf, orcamento, l, 70, somapeca, somaservicos)
                s.setStyle(table_styleservico)
                s.wrapOn(pdf, width, height)
                s.drawOn(pdf, 39, y)
                self.paginacao(pdf, countpage)
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
                f = Table(
                    pecas,
                    colWidths=[4.18 * inch, 0.5 * inch, 0.5 * inch, 1 * inch, 1 * inch],
                    rowHeights=0.2 * inch,
                )
                s = Table(
                    servicos,
                    colWidths=[6.18 * inch, 1 * inch],
                    rowHeights=0.2 * inch,
                )
                self.tabelas_pos(pdf, orcamento, l, 70, somapeca, somaservicos)
                f.setStyle(table_stylepecas)
                s.setStyle(table_styleservico)
                s.wrapOn(pdf, width, height)
                f.wrapOn(pdf, width, height)
                f.drawOn(pdf, 39, y)
                s.drawOn(pdf, 39, z)
                self.paginacao(pdf, countpage)
        pdf.save()
        if path:
            os.startfile(f"{path}\\{nomearquivo}")
        else:
            os.startfile(f"{os.path.expandvars('%LOCALAPPDATA%')}\Temp\\{nomearquivo}")