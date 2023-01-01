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

#Rótulo --> Label
#Entry --> Campo de Texto 
#Button --> Botão 
#Text --> área de texto
#place --> Método para definir um elemento gráfico

#Visualizar Dados
def Visualizar_Dados():

    sql = "select * from pedidos" #Consulta SQL de retorno de dados
    cursor.execute(sql)

    result = cursor.fetchall()
    texto = "" #Variável auxiliar
    
    for linha in result:
        texto = texto + f"------------------------------------------------------------------------------ \nNome do Cliente: {str(linha[0])} \nPedido: {str(linha[1])} \nQuantidade: {str(linha[2])} \nValor Unitário: {str(linha[3])} \nValor total: {(linha[3])*(linha[2])} \n------------------------------------------------------------------------------ \n\n" # str - Converte em string
        #print(f'Nome do Cliente: {linha[0]} - Pedido: {linha[1]} - Quantidade: {linha[2]} - Valor Unitário: {linha[3]}')

    aba2_Texto.delete(1.0, 'end') #Deletar informações contidas no campo
    aba2_Texto.insert(END, texto) #Inserir Informações

#Atualizar Dados
def Atualizar_Dados():
    #Procedimento para captura dos dados digitados pelo usuário
    cliente = aba3_ClienteEntry.get()
    novo_pedido = aba3_NovoPedidoEntry.get()
    nova_quantidade = aba3_NovaQuantidadeEntry.get()
    novo_valor = aba3_NovoValorEntry.get()

    #print(f"Nome do Cliente: {cliente} - Novo pedido: {novo_pedido} - Nova Quantidade: {nova_quantidade} - Novo Valor Unitário: {novo_valor}")

    sql = f"update pedidos set pedido = '{novo_pedido}', quantidade = {nova_quantidade}, valor = {novo_valor} where cliente = '{cliente}'"

    #print(sql)

    cursor.execute(sql)
    conexao.commit() 

    Limpar_Dados_Aba3()
    
#Inserir dados no Banco de Dados - PostgreSQL
def Inserir_Dados():
    #Obter os dados no campo da aplicação:
    cliente = aba1_ClienteEntry.get() #Obtém o nome do cliente
    pedido = aba1_PedidoEntry.get() #Obtém o pedido do cliente
    quantidade = aba1_QuantidadeEntry.get() #Obtém a quantidade de pedidos
    valor = aba1_ValorEntry.get() #Obtém o valor do pedido

    #print(f"Nome do Cliente: {cliente} - Pedido: {pedido} - Quantidade: {quantidade} - Valor: {valor}")
    
    #Construção da consulta SQL
    sql = f"insert into pedidos values ('{cliente}','{pedido}',{quantidade},{valor})"
    
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

#Limpar Dados da Aba 3:
def Limpar_Dados_Aba3():
    aba3_ClienteEntry.delete(0, 'end')
    aba3_NovoPedidoEntry.delete(0, 'end')
    aba3_NovaQuantidadeEntry.delete(0, 'end')
    aba3_NovoValorEntry.delete(0, 'end')

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

#######################################################################################################################################################
def Gerar_Relatorio():
    try:
        #Endereço onde o arquivo será criado + nome do arquivo
        end_arq = "C:\\Users\\55849\\Downloads\\relatorio_animes.pdf"
        
        #Criação do arquivo pdf:
        pdf = canvas.Canvas(end_arq, pagesize = A4)
        #Metadados sobre o arquivo:
        pdf.setTitle('Relatório de Animes')
        pdf.setAuthor('Débora e Deivid')
        pdf.setKeywords('Anime, Donghua, Animação, Japão, China')
        
        ##Escrevendo o conteúdo do arquivo pdf##
        #Definição da fonte e do tamanho da letra:
        pdf.setFont('Times-Bold', 20)
        #Definição de um título para o arquivo pdf:
        pdf.drawCentredString(width/2, 760, "Animes e Donghuas")
        
        #Definição de um subtítulo para o arquivo pdf:
        pdf.setFont('Times-Roman', 15)
        pdf.setFillColor(colors.brown) #Definição da cor da fonte
        pdf.drawCentredString(width/2, 730, "Japão, China e suas animações")
        
        #Desenhando uma linha horizontal:
        pdf.line(30, 700, 550, 700) #Coordenadas iniciais e finais da linha

        ##Inserção de um parágrafo:##
        #Escrevendo o texto:
        paragrafo = ['Os emocionantes animes, são as animações produzidas por estúdios do Japão.', 'Uma variação disso seriam os Donghuas, que são justamente as animações produzidas por estúdios da', 'China!!  Ambos com suas particularidades e com uma grande diversidade de gêneros, para todos os gostos.', 'Aqui você irá encontrar as melhores indicações de Animes e Donghuas, como também informações', 'ao seu respeito, personagens que mais nos cativam e muito mais!', ' ', 'Esperamos que possam se sentir estimulados a assistí-los e que, as informações aqui contidas, possam', 'ajudá-los a conhecer um poucos mais essas maravilhosas obras!!'] #As informações dentro das aspas, representa uma linha do arquivo pdf.

        #Definindo onde esse texto irá começar:
        text = pdf.beginText(40, 680)

        #Definindo o tipo da fonte:
        text.setFont('Times-Roman', 12)
        text.setFillColor(colors.black) #Definindo a cor da fonte
        
        #Adicionando uma lista de itens:
        text.textLines(paragrafo)
        pdf.drawText(text)

        #Lista de valores:
        dados = [
            ['Código do Anime', 'Nome do Anime', 'Temporadas', 'Episódios', 'Personagem Favorito¹', 'Personagem Favorito²'],
        ]

        #Definição da consulta SQL que retorna todos os dados da tabela 'animes':
        sql = 'select * from animes'

        cursor.execute(sql)
        resultado = cursor.fetchall() #Lista de itens que estão no Banco de Dados
        #print(resultado)
        for linha in resultado:
            #print("-------------------------------------------------------------------------------------------------------------------------------------")
            cod = str(linha[0]) #Coluna onde está o código
            n = str(linha[1]) #Coluna onde está o nome
            temp = str(linha[2]) #Coluna onde está as temporadas
            ep = str(linha[3]) #Coluna onde está os episódios
            pf1 = str(linha[4]) #Coluna onde está o personagem fav1
            pf2 = str(linha[5]) #Coluna onde está o personagem fav2
            #print(f"Código: {cod} - Nome: {n} - Temporadas: {temp} - Episódios: {ep} - Personagem Favorito¹: {pf1} - Personagem Favorito²: {pf2}")
            #Item que contém os dados que estão vindo do Banco de Dados:
            item = [cod, n, temp, ep, pf1, pf2]
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
        tabela.drawOn(pdf, 30, 380) 
        
        #Inserir uma imagem:
        imagem1 = "C:\\Users\\debor\\OneDrive\\Documentos\\IFRN\\Programação com Acesso a Banco de Dados\\Projeto\\1.jpg"
        imagem2 = "C:\\Users\\debor\\OneDrive\\Documentos\\IFRN\\Programação com Acesso a Banco de Dados\\Projeto\\2.jpg"
        pdf.drawInlineImage(imagem1, 35, 710)
        pdf.drawInlineImage(imagem2, 450, 710)

        #Salvando o arquivo:
        pdf.save()

        messagebox.showinfo('Sucesso!', 'Relatório gerado com sucesso.')
    except:
        messagebox.showerror('Erro!', 'Não foi possível gerar Relatório.')
####################################################################################################################################################

janela = Tk() #Janela recebe uma instância de Tk()

#Gerenciador de Abas
gerenciadorAba = ttk.Notebook(janela)

#Aba 1 - Inserir Dados
aba1 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba1, text = "Inserir Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 1 #
aba1_ClienteLabel = Label(aba1, text = "Nome do Cliente:")
aba1_ClienteLabel.place(x = 100, y = 80)

aba1_ClienteEntry = Entry(aba1)
aba1_ClienteEntry.place(x = 100, y = 100)

aba1_PedidoLabel = Label(aba1, text = "Pedido:")
aba1_PedidoLabel.place(x = 400, y = 80)

aba1_PedidoEntry = Entry(aba1)
aba1_PedidoEntry.place(x = 400, y = 100)

aba1_QuantidadeLabel = Label(aba1, text = "Quantidade:")
aba1_QuantidadeLabel.place(x = 100 , y = 180)

aba1_QuantidadeEntry = Entry(aba1)
aba1_QuantidadeEntry.place(x = 100, y = 200)

aba1_ValorLabel = Label(aba1, text = "Valor Unitário:")
aba1_ValorLabel.place(x = 400 , y = 180)

aba1_ValorEntry = Entry(aba1)
aba1_ValorEntry.place(x = 400 , y = 200)

aba1_CadastrarButton = Button(aba1, width = 16, text = "Cadastrar Pedido", command = Inserir_Dados)
aba1_CadastrarButton.place(x = 100 , y = 300)

aba1_LimparDados = Button(aba1, width = 16, text = "Limpar Dados", command = Limpar_Dados_Aba1)
aba1_LimparDados.place(x = 400, y = 300)

#Aba 2 - Visualizar Dados:
aba2 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba2, text = "Visualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 2 ##
aba2_TextoLabel = Label(aba2 , text = "Pedidos Cadastrados:")
aba2_TextoLabel.place(x = 100 , y = 80)

aba2_VisualizarButton = Button(aba2, width = 20, text = "Visualizar Dados", command = Visualizar_Dados)
aba2_VisualizarButton.place(x = 300, y = 70)

aba2_RelatorioButton = Button(aba2, width = 20, text = "Gerar Relatório", command = Gerar_Relatorio)
aba2_RelatorioButton.place(x = 500, y = 70)

aba2_Texto = Text(aba2)
aba2_Texto.place(x = 100 , y = 120)

#Aba 3 - Atualizar Dados:
aba3 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba3, text = "Atualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 3 ###
aba3_ClienteLabel = Label(aba3, text = "Nome do Cliente:")
aba3_ClienteLabel.place(x = 100, y = 80)

aba3_ClienteEntry = Entry(aba3, width = 30)
aba3_ClienteEntry.place(x = 100 , y = 100)

aba3_NovoPedidoLabel = Label(aba3, text = "Novo Pedido:")
aba3_NovoPedidoLabel.place(x = 400, y = 80)

aba3_NovoPedidoEntry = Entry(aba3, width = 30)
aba3_NovoPedidoEntry.place(x = 400, y = 100)

aba3_NovaQuantidadeLabel = Label(aba3, text = "Nova quantidade:")
aba3_NovaQuantidadeLabel.place(x = 100, y = 180)

aba3_NovaQuantidadeEntry = Entry(aba3, width = 30)
aba3_NovaQuantidadeEntry.place(x = 100, y = 200)

aba3_NovoValorLabel = Label(aba3, text = "Novo Valor Unitário:")
aba3_NovoValorLabel.place(x = 400 , y = 180)

aba3_NovoValorEntry = Entry(aba3, width = 30)
aba3_NovoValorEntry.place(x = 400, y = 200)

aba3_AtualizarButton = Button(aba3, width = 25, text = "Atualizar Dados", command = Atualizar_Dados)
aba3_AtualizarButton.place(x = 100, y = 400)

aba3_LimparDadosButton = Button(aba3, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba3)
aba3_LimparDadosButton.place(x = 400, y = 400)

#Aba 4 - Remover Dados:
aba4 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba4, text = "Remover Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 4 ####
aba4_ClienteLabel = Label(aba4, text = "Nome do Cliente:")
aba4_ClienteLabel.place(x = 230, y = 180)

aba4_ClienteEntry = Entry(aba4)
aba4_ClienteEntry.place(x = 340, y = 180)

aba4_RemoverButton = Button(aba4, width = 25, text = "Remover Cliente", command = Remover_Dados)
aba4_RemoverButton.place(x = 100, y = 240)

aba4_LimparDadosButton = Button(aba4, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba4)
aba4_LimparDadosButton.place(x = 400, y = 240)

#Definição das dimensões da janela
janela.geometry("800x600+0+0")
janela.mainloop()
