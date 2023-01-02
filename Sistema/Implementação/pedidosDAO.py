#DAO (Data Access Object

import psycopg2

class PedidosDAO:

    def __init__(self):
        self.conexao = psycopg2.connect(database = "PDS", user = "postgres", password = "kluyvert", host = "localhost", port = "5432")
        self.cursor = self.conexao.cursor()
    
    #Método para inserir o Pedido no Banco de Dados:
    def Inserir_Pedido(self, pedidos):
        sql = f"insert into pedidos values ('{pedidos.getCliente()}', '{pedidos.getPedido()}' ,{pedidos.getQuantidade()}, {pedidos.getValor()})"
        self.cursor.execute(sql)
        self.conexao.commit()
