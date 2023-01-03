#Mapeamento da tabela 'pedidos' que está no banco de dados:
class PedidosBean:
  def_init_(self):
    self.__cliente = None #Atributo Privado
    self.__pedido = None #Atributo Privado
    self.__quantidade = None #Atributo Privado
    self.__Valor = None #Atributo Privado
    
    #Retorna o nome do cliente, pois ele foi definido como privado:
    
    def getCliente(self):
      return self.__cliente
    def getPedido(self):
      return self.__pedido
    def getQuantidade(self):
      return self.__quantidade
    def getValor(self):
      return self.__valor
    
    #Definindo os métodos set, pois os atributos foram declarados como privados:
    def setCliente(self, cll):
      self.__cliente = cli
    def setPedido(self, p):
      self.__pedido =  p
    def setQuantidade(self, quant):
      self.__quantidade = quant
    def setValor(self, val):
      self.__valor = val
