#Importação da Biblioteca tkinter
from tkinter import *
from tkinter import ttk #Módulo complementar ao tkinter

#Importação da Biblioteca psycopg2
import psycopg2

#Estabelecer uma conexão com o Banco de Dados - PostgreSQL
conexao = psycopg2.connect(database = "PDS", user = "postgres", password = "kluyvert", host = "localhost", port = "5432")

#Definição do cursor
cursor = conexao.cursor()

#Visualizar Dados
def Visualizar_Dados():

    sql = "select * from pedidos" #Consulta SQL de retorno de dados
    cursor.execute(sql)

    result = cursor.fetchall()
    texto = "" #Variável auxiliar
    
    for linha in result:
        texto = texto + f"------------------------------------------------------------------------------ \nNome do Cliente: {str(linha[0])} \nPedido: {str(linha[1])} \nQuantidade: {str(linha[2])} \nValor Unitário: {str(linha[3])}\n------------------------------------------------------------------------------ \n\n" # str - Converte em string
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

////////////////////////////////////////////////////////////////////////////////////////
#Limpar dados da Aba 1:
def Limpar_Dados_Aba1():
    aba1_ClienteEntry.delete(0, 'end')
    aba1_NomeEntry.delete(0, 'end')
    aba1_QuantidadeEntry.delete(0, 'end')
    aba1_ValorEntry.delete(0, 'end')
    aba1_EnderecoEntry.delete(0, 'end')
    aba1_ClienteEntry.delete(0, 'end')

#Limpar Dados da Aba 3:
def Limpar_Dados_Aba3():
    aba3_NumeroEntry.delete(0, 'end')
    aba3_NovoPedidoEntry.delete(0, 'end')
    aba3_NovaQuantidadeEntry.delete(0, 'end')
    aba3_NovoValorEntry.delete(0, 'end')
    aba3_NovoEnderecoEntry.delete(0, 'end')
    aba3_NovoClienteEntry.delete(0, 'end')

#Limpar Dados da Aba 4
def Limpar_Dados_Aba4():
    aba4_NumeroEntry.delete(0,'end')

#Remover Dados do Banco de Dados
def Remover_Dados():
    numero = aba4_NumeroEntry.get()

    sql = f"delete from pedidos where numero = {numero}"

    cursor.execute(sql)
    conexao.commit()

    Limpar_Dados_Aba4()

janela = Tk() #Janela recebe uma instância de Tk()

#Gerenciador de Abas
gerenciadorAba = ttk.Notebook(janela)

#Aba 1 - Inserir Dados
aba1 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba1, text = "Inserir Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 1 #
aba1_NumeroLabel = Label(aba1, text = "Pedido Nº:")
aba1_NumeroLabel.place(x = 100, y = 80)

aba1_NumeroEntry = Entry(aba1)
aba1_NumeroEntry.place(x = 100, y = 100)

aba1_NomeLabel = Label(aba1, text = "Pedido:")
aba1_NomeLabel.place(x = 400, y = 80)

aba1_NomeEntry = Entry(aba1)
aba1_NomeEntry.place(x = 400, y = 100)

aba1_TemporadasLabel = Label(aba1, text = "Temporadas:")
aba1_TemporadasLabel.place(x = 100 , y = 180)

aba1_TemporadasEntry = Entry(aba1)
aba1_TemporadasEntry.place(x = 100, y = 200)

aba1_EpisodiosLabel = Label(aba1, text = "Episódios:")
aba1_EpisodiosLabel.place(x = 400 , y = 180)

aba1_EpisodiosEntry = Entry(aba1)
aba1_EpisodiosEntry.place(x = 400 , y = 200)

aba1_PersonagemFav1Label = Label(aba1, text = "Personagem Favorito¹:")
aba1_PersonagemFav1Label.place(x = 100 , y = 280)

aba1_PersonagemFav1Entry = Entry(aba1)
aba1_PersonagemFav1Entry.place(x = 100 , y = 300)

aba1_PersonagemFav2Label = Label(aba1, text = "Personagem Favorito²:")
aba1_PersonagemFav2Label.place(x = 400 , y = 280 )

aba1_PersonagemFav2Entry = Entry(aba1)
aba1_PersonagemFav2Entry.place(x = 400 , y = 300)

aba1_CadastrarButton = Button(aba1, width = 16, text = "Cadastrar Anime", command = Inserir_Dados)
aba1_CadastrarButton.place(x = 100 , y = 400)

aba1_LimparDados = Button(aba1, width = 16, text = "Limpar Dados", command = Limpar_Dados_Aba1)
aba1_LimparDados.place(x = 400, y = 400)

#Aba 2 - Visualizar Dados:
aba2 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba2, text = "Visualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 2 ##
aba2_TextoLabel = Label(aba2 , text = "Animes Cadastrados:")
aba2_TextoLabel.place(x = 100 , y = 80)

aba2_VisualizarButton = Button(aba2, width = 20, text = "Visualizar Dados", command = Visualizar_Dados)
aba2_VisualizarButton.place(x = 300, y = 70)

aba2_Texto = Text(aba2)
aba2_Texto.place(x = 100 , y = 120)

#Aba 3 - Atualizar Dados:
aba3 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba3, text = "Atualizar Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 3 ###
aba3_CodigoLabel = Label(aba3, text = "Código do Anime:")
aba3_CodigoLabel.place(x = 100, y = 80)

aba3_CodigoEntry = Entry(aba3, width = 30)
aba3_CodigoEntry.place(x = 100 , y = 100)

aba3_NovoAnimeLabel = Label(aba3, text = "Novo Nome do Anime:")
aba3_NovoAnimeLabel.place(x = 400, y = 80)

aba3_NovoAnimeEntry = Entry(aba3, width = 30)
aba3_NovoAnimeEntry.place(x = 400, y = 100)

aba3_NovaTemporadaLabel = Label(aba3, text = "Novo Número de Temporadas:")
aba3_NovaTemporadaLabel.place(x = 100, y = 180)

aba3_NovaTemporadaEntry = Entry(aba3, width = 30)
aba3_NovaTemporadaEntry.place(x = 100, y = 200)

aba3_NovosEpisodiosLabel = Label(aba3, text = "Novo Número de Episódios:")
aba3_NovosEpisodiosLabel.place(x = 400 , y = 180)

aba3_NovosEpisodiosEntry = Entry(aba3, width = 30)
aba3_NovosEpisodiosEntry.place(x = 400, y = 200)

aba3_NovoPF1Label = Label(aba3, text = "Novo Personagem Favorito¹:")
aba3_NovoPF1Label.place(x = 100, y = 280)

aba3_NovoPF1Entry = Entry(aba3, width = 30)
aba3_NovoPF1Entry.place(x = 100, y = 300)

aba3_NovoPF2Label = Label(aba3, text = "Novo Personagem Favorito²:")
aba3_NovoPF2Label.place(x = 400, y = 280)

aba3_NovoPF2Entry = Entry(aba3, width = 30)
aba3_NovoPF2Entry.place(x = 400, y = 300)

aba3_AtualizarButton = Button(aba3, width = 25, text = "Atualizar Dados", command = Atualizar_Dados)
aba3_AtualizarButton.place(x = 100, y = 400)

aba3_LimparDadosButton = Button(aba3, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba3)
aba3_LimparDadosButton.place(x = 400, y = 400)

#Aba 4 - Remover Dados:
aba4 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba4, text = "Remover Dados")
gerenciadorAba.pack(expand = 1, fill = "both")

## Elementos da Aba 4 ####
aba4_CodigoLabel = Label(aba4, text = "Código do Anime:")
aba4_CodigoLabel.place(x = 230, y = 180)

aba4_CodigoEntry = Entry(aba4)
aba4_CodigoEntry.place(x = 340, y = 180)

aba4_RemoverButton = Button(aba4, width = 25, text = "Remover Anime", command = Remover_Dados)
aba4_RemoverButton.place(x = 100, y = 240)

aba4_LimparDadosButton = Button(aba4, width = 25, text = "Limpar Dados", command = Limpar_Dados_Aba4)
aba4_LimparDadosButton.place(x = 400, y = 240)

#Definição das dimensões da janela
janela.geometry("800x600+0+0")
janela.mainloop()
