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
