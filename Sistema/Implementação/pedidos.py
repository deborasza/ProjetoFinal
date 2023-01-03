#Importação da Biblioteca tkinter
from tkinter import *
from tkinter import ttk #Módulo complementar ao tkinter

#Importação da Biblioteca psycopg2
import psycopg2

#Gerar log de erro
import traceback

#Gerar janelas informativas para o usuário
from tkinter import messagebox

#Importação da Biblioteca reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

#Estabelecer uma conexão com o Banco de Dados - PostgreSQL
conexao = psycopg2.connect(database = "PDS", user = "postgres", password = "kluyvert", host = "localhost", port = "5432")
#Definição do cursor
cursor = conexao.cursor()

from turtle import width 
width, height = A4
    
#Inserir dados no Banco de Dados - PostgreSQL
def Inserir_Dados():
    #Obter os dados no campo da aplicação:
    cliente = aba1_ClienteEntry.get() #Obtém o nome do cliente
    pedido = aba1_PedidoEntry.get() #Obtém o pedido do cliente
    quantidade = aba1_QuantidadeEntry.get() #Obtém a quantidade de pedidos
    valor_unitario = aba1_ValorEntry.get() #Obtém o valor do pedido
    valor_total = (int(valor_unitario))*(int(quantidade))
    rua = aba1_RuaEntry.get() #Obtém o endereço para entrega do pedido
    n_casa = aba1_NumeroCasaEntry.get() #Obtém o número da casa do cliente
    bairro = aba1_BairroEntry.get() #Obtém o nome do bairro do cliente
    cep = aba1_CEPEntry.get() #Obtém o CEP do endereço para entrega do pedido

    #Construção da consulta SQL
    sql = f"insert into pedidos values ('{cliente}','{pedido}',{quantidade},{valor_unitario},{valor_total},'{rua}',{n_casa},'{bairro}',{cep})"
    
    #Procedimento para executar a consulta
    cursor.execute(sql)
    conexao.commit()

    #Limpar dados da aba1
    Limpar_Dados_Aba1()

#Limpar dados da Aba 1:
def Limpar_Dados_Aba1():
    aba1_ClienteEntry.delete(0, 'end')
    aba1_PedidoEntry.delete(0, 'end')
    aba1_QuantidadeEntry.delete(0, 'end')
    aba1_ValorEntry.delete(0, 'end')
    aba1_RuaEntry.delete(0, 'end')
    aba1_NumeroCasaEntry.delete(0, 'end')
    aba1_BairroEntry.delete(0, 'end')
    aba1_CEPEntry.delete(0, 'end')

#Visualizar Dados
def Visualizar_Dados():

    sql = "select * from pedidos" #Consulta SQL de retorno de dados
    cursor.execute(sql)

    result = cursor.fetchall()
    texto = "" #Variável auxiliar
    
    for linha in result:
        texto = texto + f"------------------------------------------------------------------------------ \nNome do Cliente: {str(linha[0])} \nPedido: {str(linha[1])} \nQuantidade: {str(linha[2])} \nValor Unitário: {str(linha[3])} \nValor total: {str(linha[4])} \nEndereço para Entrega: {str(linha[5])}, {str(linha[6])}, {str(linha[7])}, {str(linha[8])} \n------------------------------------------------------------------------------ \n\n" # str - Converte em string
        #print(f'Nome do Cliente: {linha[0]} - Pedido: {linha[1]} - Quantidade: {linha[2]} - Valor Unitário: {linha[3]} - Valor Total: {(linha[4]} - Endereço para Entrega: ])}, {str(linha[7])}, {str(linha[8])}')

    aba2_Texto.delete(1.0, 'end') #Deletar informações contidas no campo
    aba2_Texto.insert(END, texto) #Inserir Informações

#Atualizar Dados
def Atualizar_Dados():
    #Procedimento para captura dos dados digitados pelo usuário
    cliente = aba3_ClienteEntry.get()
    novo_pedido = aba3_NovoPedidoEntry.get()
    nova_quantidade = aba3_NovaQuantidadeEntry.get()
    novo_valor = aba3_NovoValorEntry.get()
    novo_valor_total = (int(novo_valor))*(int(nova_quantidade))
    nova_rua = aba3_NovaRuaEntry.get()
    novo_numero = aba3_NovoNumeroEntry.get()
    novo_bairro = aba3_NovoBairroEntry.get()
    novo_cep = aba3_NovoCEPEntry.get()

    sql = f"update pedidos set pedido = '{novo_pedido}', quantidade = {nova_quantidade}, valor_unitario = {novo_valor}, valor_total = {novo_valor_total}, rua = '{nova_rua}', n_casa = {novo_numero}, bairro = '{novo_bairro}', cep = {novo_cep} where cliente = '{cliente}'"

    #print(sql)

    cursor.execute(sql)
    conexao.commit() 

    Limpar_Dados_Aba3()

#Limpar Dados da Aba 3:
def Limpar_Dados_Aba3():
    aba3_ClienteEntry.delete(0, 'end')
    aba3_NovoPedidoEntry.delete(0, 'end')
    aba3_NovaQuantidadeEntry.delete(0, 'end')
    aba3_NovoValorEntry.delete(0, 'end')
    aba3_NovaRuaEntry.delete(0, 'end')
    aba3_NovoNumeroEntry.delete(0, 'end')
    aba3_NovoBairroEntry.delete(0, 'end')
    aba3_NovoCEPEntry.delete(0, 'end')

#Limpar Dados da Aba 4
def Limpar_Dados_Aba4():
    aba4_ClienteEntry.delete(0,'end')

#Remover Dados do Banco de Dados
def Remover_Dados():
    cliente = aba4_ClienteEntry.get()

    sql = f"delete from pedidos where cliente = '{cliente}'"
    
    #Tratamento de erros:
    try:
        cursor.execute(sql)
        conexao.commit()
        #Mensagem mostrada para o usuário, caso a operação funcione:
        messagebox.showinfo('Sucesso!', 'Operação realizada com sucesso.')
    except:
        conexao.rollback()
        traceback.print_exc()
        #Mensagem mostrada para o usuário, caso a operação dê erro:
        messagebox.showerror('Erro!', 'Operação mal sucedida!')
    finally:
        Limpar_Dados_Aba4()

def Gerar_Relatorio():
    try:
        #Endereço onde o arquivo será criado + nome do arquivo
        end_arq = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Relatório\\relatorio_pedidos.pdf"
        
        #Criação do arquivo pdf:
        pdf = canvas.Canvas(end_arq, pagesize = A4)
        #Metadados sobre o arquivo:
        pdf.setTitle('Relatório de Pedidos')
        pdf.setAuthor('Débora, Deivid, Giovanna e Isabel')
        pdf.setKeywords('Queijo, CT, Sistema, Python, Cadastro, Pedidos')
        
        ##Escrevendo o conteúdo do arquivo pdf##
        #Definição da fonte e do tamanho da letra:
        pdf.setFont('Times-Bold', 20)
        #Definição de um título para o arquivo pdf:
        pdf.drawCentredString(width/2, 735, "Relatório de Pedidos")
        
        #Definição de um subtítulo para o arquivo pdf:
        pdf.setFont('Times-Roman', 15)
        pdf.setFillColor(colors.brown) #Definição da cor da fonte
        pdf.drawCentredString(width/2, 710, "Centro de Tecnologia do Queijo - Campus Currais Novos")
        
        #Desenhando uma linha horizontal:
        pdf.line(30, 695, 550, 695) #Coordenadas iniciais e finais da linha

        ##Inserção de um parágrafo:##
        #Escrevendo o texto:
        paragrafo = ['Tabela de pedidos realizados e suas devidas informações:'] #As informações dentro das aspas, representa uma linha do arquivo pdf.

        #Definindo onde esse texto irá começar:
        text = pdf.beginText(40, 675)

        #Definindo o tipo da fonte:
        text.setFont('Times-Roman', 12)
        text.setFillColor(colors.black) #Definindo a cor da fonte
        
        #Adicionando uma lista de itens:
        text.textLines(paragrafo)
        pdf.drawText(text)

        #Lista de valores:
        dados = [
            ['Nome do Cliente', 'Pedido', 'Quantidade', 'Valor Unitário', 'Valor Total'],
        ]

        #Definição da consulta SQL que retorna todos os dados da tabela 'animes':
        sql = 'select cliente, pedido, quantidade, valor_unitario, valor_total from pedidos'

        cursor.execute(sql)
        resultado = cursor.fetchall() #Lista de itens que estão no Banco de Dados
        #print(resultado)
        for linha in resultado:
            #print("-------------------------------------------------------------------------------------------------------------------------------------")
            cli = str(linha[0]) #Coluna onde está o nome do cliente
            p = str(linha[1]) #Coluna onde está o pedido
            quant = str(linha[2]) #Coluna onde está a quantidade
            vu = str(linha[3]) #Coluna onde está o valor
            vt = str(linha[4]) #Coluna onde está o valor total
            #Item que contém os dados que estão vindo do Banco de Dados:
            item = [cli, p, quant, vu, vt]
            #Adição do item ao conjunto de dados:
            dados.append(item)

        #Criação da tabela:
        tabela = Table(dados)

        #Montando item por item
        estilo = TableStyle([
            #Cor de fundo da primeira linha:
            ('BACKGROUND', (0,0), (6,0), colors.brown), 
            #Cor do texto da primeira linha:
            ('TEXTCOLOR', (0,0), (6,0), colors.whitesmoke), 
            #Fonte da tabela inteira:
            ('FONTNAME', (0,0), (6,-1), 'Courier-Bold'), #-1 representa o último elemento
            #Tamanho da fonte:
            ('FONTSIZE', (0,0), (6,-1), 8.5),
            #Alinhamento do texto:
            ('ALIGN', (0,0), (6,-1), 'CENTER'),
            #Cor de fundo dos dados:
            ('BACKGROUND', (0,1), (6,-1), colors.beige),
            #Cor do texto dos dados:
            ('TEXTCOLOR', (0,1), (6,-1), colors.black),
            #Tamanho e cor da borda:
            ('GRID', (0,0), (6,-1), 0.5, colors.brown)
        ])
        #Adicionar estilo à tabela:
        tabela.setStyle(estilo)

        #Tamanho da tabela:
        tabela.wrapOn(pdf, 400, 100)
        #Posicionamento da tabela:
        tabela.drawOn(pdf, 30, 585) 

        #Inserir uma imagem:
        imagem1 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\1.png"
        imagem2 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\2.jpg"
        imagem3 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\3.jpeg"
        pdf.drawInlineImage(imagem1, 240, 760)
        pdf.drawInlineImage(imagem2, width/2, 770)
        pdf.drawInlineImage(imagem3, 330, 760)

        #Salvando o arquivo:
        pdf.save()

        #Exibindo caixa de mensagem:
        messagebox.showinfo('Sucesso!', 'Relatório gerado com sucesso.')
    except:
        messagebox.showerror('Erro!', 'Não foi possível gerar Relatório.')

def Gerar_ListaDeEntrega():
    try:
        #Endereço onde o arquivo será criado + nome do arquivo
        end_arq = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Lista de Entrega\\lista_entrega.pdf"
        
        #Criação do arquivo pdf:
        pdf = canvas.Canvas(end_arq, pagesize = A4)
        #Metadados sobre o arquivo:
        pdf.setTitle('Lista de Entrega para Motorista')
        pdf.setAuthor('Débora, Deivid, Giovanna e Isabel')
        pdf.setKeywords('Queijo, CT, Sistema, Python, Cadastro, Pedidos')
        
        ##Escrevendo o conteúdo do arquivo pdf##
        #Definição da fonte e do tamanho da letra:
        pdf.setFont('Times-Bold', 20)
        #Definição de um título para o arquivo pdf:
        pdf.drawCentredString(width/2, 750, "Lista de Entrega")
        
        #Definição de um subtítulo para o arquivo pdf:
        pdf.setFont('Times-Roman', 15)
        pdf.setFillColor(colors.brown) #Definição da cor da fonte
        pdf.drawCentredString(width/2, 725, "CT do Queijo, IFRN - Campus Currais Novos")
        
        #Desenhando uma linha horizontal:
        pdf.line(30, 705, 550, 705) #Coordenadas iniciais e finais da linha

        ##Inserção de um parágrafo:##
        #Escrevendo o texto:
        paragrafo = ['Tabela de endereços para entrega de pedidos:'] #As informações dentro das aspas, representa uma linha do arquivo pdf.

        #Definindo onde esse texto irá começar:
        text = pdf.beginText(40, 685)

        #Definindo o tipo da fonte:
        text.setFont('Times-Roman', 12)
        text.setFillColor(colors.black) #Definindo a cor da fonte
        
        #Adicionando uma lista de itens:
        text.textLines(paragrafo)
        pdf.drawText(text)

        #Lista de valores:
        dados = [
            ['Nome do Cliente', 'Pedido', 'Rua', 'Nº da Casa', 'Bairro', 'CEP'],
        ]

        #Definição da consulta SQL que retorna todos os dados da tabela 'animes':
        sql = 'select cliente, pedido, quantidade, rua, n_casa, bairro, cep from pedidos'

        cursor.execute(sql)
        resultado = cursor.fetchall() #Lista de itens que estão no Banco de Dados
        #print(resultado)
        for linha in resultado:
            #print("-------------------------------------------------------------------------------------------------------------------------------------")
            cli = str(linha[0]) #Coluna onde está o nome do cliente
            p = str(linha[1]) #Coluna onde está o pedido
            quant = str(linha[2]) #Coluna onde está a quantidade
            rua = str(linha[3]) #Coluna onde está a rua
            n_casa = str(linha[4]) #Coluna onde está o número da casa
            bairro = str(linha[5]) #Coluna onde está o bairro 
            cep = str(linha[6]) #Coluna onde está o CEP
            #Item que contém os dados que estão vindo do Banco de Dados:
            item = [cli, p, quant, rua, n_casa, bairro, cep]
            #Adição do item ao conjunto de dados:
            dados.append(item)

        #Criação da tabela:
        tabela = Table(dados)

        #Montando item por item
        estilo = TableStyle([
            #Cor de fundo da primeira linha:
            ('BACKGROUND', (0,0), (6,0), colors.brown), 
            #Cor do texto da primeira linha:
            ('TEXTCOLOR', (0,0), (6,0), colors.whitesmoke), 
            #Fonte da tabela inteira:
            ('FONTNAME', (0,0), (6,-1), 'Courier-Bold'), #-1 representa o último elemento
            #Tamanho da fonte:
            ('FONTSIZE', (0,0), (6,-1), 8.5),
            #Alinhamento do texto:
            ('ALIGN', (0,0), (6,-1), 'CENTER'),
            #Cor de fundo dos dados:
            ('BACKGROUND', (0,1), (6,-1), colors.beige),
            #Cor do texto dos dados:
            ('TEXTCOLOR', (0,1), (6,-1), colors.black),
            #Tamanho e cor da borda:
            ('GRID', (0,0), (6,-1), 0.5, colors.brown)
        ])
        #Adicionar estilo à tabela:
        tabela.setStyle(estilo)

        #Tamanho da tabela:
        tabela.wrapOn(pdf, 400, 100)
        #Posicionamento da tabela:
        tabela.drawOn(pdf, 30, 585) 

        #Inserir uma imagem:
        imagem1 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\1.png"
        imagem2 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\2.jpg"
        imagem3 = "C:\\Users\\55849\\Documents\\ProjetoFinal\\Sistema\\Imagens\\3.jpeg"
        pdf.drawInlineImage(imagem1, 240, 780)
        pdf.drawInlineImage(imagem2, width/2, 790)
        pdf.drawInlineImage(imagem3, 330, 780)

        #Salvando o arquivo:
        pdf.save()

        #Exibindo caixa de mensagem
        messagebox.showinfo('Sucesso!', 'Lista gerada com sucesso.')
    except:
        messagebox.showerror('Erro!', 'Não foi possível gerar Lista.')

janela = Tk() #Janela recebe uma instância de Tk()

#Gerenciador de Abas
gerenciadorAba = ttk.Notebook(janela)

#Aba 1 - Inserir Dados
aba1 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba1, text = "Inserir Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 1 #
aba1_ClienteLabel = Label(aba1, text = "Nome Completo do Cliente:")
aba1_ClienteLabel.place(x = 100, y = 80)

aba1_ClienteEntry = Entry(aba1, width = 30)
aba1_ClienteEntry.place(x = 100, y = 100)

aba1_PedidoLabel = Label(aba1, text = "Pedido:")
aba1_PedidoLabel.place(x = 400, y = 80)

aba1_PedidoEntry = Entry(aba1, width = 30)
aba1_PedidoEntry.place(x = 400, y = 100)

aba1_QuantidadeLabel = Label(aba1, text = "Quantidade:")
aba1_QuantidadeLabel.place(x = 100 , y = 140)

aba1_QuantidadeEntry = Entry(aba1, width = 30)
aba1_QuantidadeEntry.place(x = 100, y = 160)

aba1_ValorLabel = Label(aba1, text = "Valor Unitário:")
aba1_ValorLabel.place(x = 400 , y = 140)

aba1_ValorEntry = Entry(aba1, width = 30)
aba1_ValorEntry.place(x = 400 , y = 160)

aba1_RuaLabel = Label(aba1, text = "Rua para Entrega:")
aba1_RuaLabel.place(x = 100 , y = 200)

aba1_RuaEntry = Entry(aba1, width = 30)
aba1_RuaEntry.place(x = 100 , y = 220)

aba1_NumeroCasaLabel = Label(aba1, text = "Nº da Casa para Entrega:")
aba1_NumeroCasaLabel.place(x = 400 , y = 200)

aba1_NumeroCasaEntry = Entry(aba1, width = 30)
aba1_NumeroCasaEntry.place(x = 400 , y = 220)

aba1_BairroLabel = Label(aba1, text = "Bairro para Entrega:")
aba1_BairroLabel.place(x = 100 , y = 260)

aba1_BairroEntry = Entry(aba1, width = 30)
aba1_BairroEntry.place(x = 100 , y = 280)

aba1_CEPLabel = Label(aba1, text = "CEP para Entrega:")
aba1_CEPLabel.place(x = 400 , y = 260)

aba1_CEPEntry = Entry(aba1, width = 30)
aba1_CEPEntry.place(x = 400 , y = 280)

aba1_CadastrarButton = Button(aba1, width = 26, text = "Cadastrar Pedido", command = Inserir_Dados)
aba1_CadastrarButton.place(x = 100 , y = 340)

aba1_LimparDados = Button(aba1, width = 26, text = "Limpar Dados", command = Limpar_Dados_Aba1)
aba1_LimparDados.place(x = 400, y = 340)

#Aba 2 - Visualizar Dados:
aba2 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba2, text = "Visualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 2 ##
aba2_TextoLabel = Label(aba2 , text = "Pedidos Cadastrados:")
aba2_TextoLabel.place(x = 100 , y = 80)

aba2_VisualizarButton = Button(aba2, width = 20, text = "Visualizar Dados", command = Visualizar_Dados)
aba2_VisualizarButton.place(x = 230, y = 70)

aba2_RelatorioButton = Button(aba2, width = 20, text = "Gerar Relatório", command = Gerar_Relatorio)
aba2_RelatorioButton.place(x = 400, y = 70)

aba2_ListaButton = Button(aba2, width = 20, text = "Gerar Lista de Entrega", command = Gerar_ListaDeEntrega)
aba2_ListaButton.place(x = 570, y = 70)

aba2_Texto = Text(aba2)
aba2_Texto.place(x = 100 , y = 120)

#Aba 3 - Atualizar Dados:
aba3 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba3, text = "Atualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 3 ###
aba3_ClienteLabel = Label(aba3, text = "Nome Completo do Cliente:")
aba3_ClienteLabel.place(x = 100, y = 80)

aba3_ClienteEntry = Entry(aba3, width = 30)
aba3_ClienteEntry.place(x = 100 , y = 100)

aba3_NovoPedidoLabel = Label(aba3, text = "Novo Pedido:")
aba3_NovoPedidoLabel.place(x = 400, y = 80)

aba3_NovoPedidoEntry = Entry(aba3, width = 30)
aba3_NovoPedidoEntry.place(x = 400, y = 100)

aba3_NovaQuantidadeLabel = Label(aba3, text = "Nova Quantidade:")
aba3_NovaQuantidadeLabel.place(x = 100, y = 140)

aba3_NovaQuantidadeEntry = Entry(aba3, width = 30)
aba3_NovaQuantidadeEntry.place(x = 100, y = 160)

aba3_NovoValorLabel = Label(aba3, text = "Novo Valor Unitário:")
aba3_NovoValorLabel.place(x = 400 , y = 140)

aba3_NovoValorEntry = Entry(aba3, width = 30)
aba3_NovoValorEntry.place(x = 400, y = 160)

aba3_NovaRuaLabel = Label(aba3, text = "Nova Rua para Entrega:")
aba3_NovaRuaLabel.place(x = 100 , y = 200)

aba3_NovaRuaEntry = Entry(aba3, width = 30)
aba3_NovaRuaEntry.place(x = 100, y = 220)

aba3_NovoNumeroLabel = Label(aba3, text = "Novo Nº da Casa para Entrega:")
aba3_NovoNumeroLabel.place(x = 400 , y = 200)

aba3_NovoNumeroEntry = Entry(aba3, width = 30)
aba3_NovoNumeroEntry.place(x = 400, y = 220)

aba3_NovoBairroLabel = Label(aba3, text = "Novo Bairro para Entrega:")
aba3_NovoBairroLabel.place(x = 100 , y = 260)

aba3_NovoBairroEntry = Entry(aba3, width = 30)
aba3_NovoBairroEntry.place(x = 100, y = 280)

aba3_NovoCEPLabel = Label(aba3, text = "Novo CEP para Entrega:")
aba3_NovoCEPLabel.place(x = 400 , y = 260)

aba3_NovoCEPEntry = Entry(aba3, width = 30)
aba3_NovoCEPEntry.place(x = 400, y = 280)

aba3_AtualizarButton = Button(aba3, width = 25, text = "Atualizar Dados", command = Atualizar_Dados)
aba3_AtualizarButton.place(x = 100, y = 340)

aba3_LimparDadosButton = Button(aba3, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba3)
aba3_LimparDadosButton.place(x = 400, y = 340)

#Aba 4 - Remover Dados:
aba4 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba4, text = "Remover Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 4 ####
aba4_ClienteLabel = Label(aba4, text = "Nome Completo do Cliente:")
aba4_ClienteLabel.place(x = 100, y = 180)

aba4_ClienteEntry = Entry(aba4, width = 54)
aba4_ClienteEntry.place(x = 260, y = 180)

aba4_RemoverButton = Button(aba4, width = 25, text = "Remover Cliente", command = Remover_Dados)
aba4_RemoverButton.place(x = 100, y = 240)

aba4_LimparDadosButton = Button(aba4, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba4)
aba4_LimparDadosButton.place(x = 400, y = 240)

#Definição das dimensões da janela
janela.geometry("800x600+0+0")
janela.mainloop()
