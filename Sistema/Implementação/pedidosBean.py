#Mapeamento da tabela 'pedidos' que está no banco de dados:
class PedidosBean:
  def _init_(self):
    self.__Cliente = None #Atributo Privado
    self.__Pedido = None #Atributo Privado
    self.__Quantidade = None #Atributo Privado
    self.__Valor = None #Atributo Privado
    self.__Rua = None #Atributo Privado
    self.__NumeroCasa = None #Atributo Privado
    self.__Bairro = None #Atributo Privado
    self.__CEP = None #Atributo Privado
    
    #Retorna o nome do cliente, pois ele foi definido como privado:
    
    def getCliente(self):
      return self.__Cliente
    def getPedido(self):
      return self.__Pedido
    def getQuantidade(self):
      return self.__Quantidade
    def getValor(self):
      return self.__Valor
    def getRua(self):
      return self.__Rua
    def getNumeroCasa(self):
      return self.__NumeroCasa
    def getBairro(self):
      return self.__Bairro
    def getCEP(self):
      return self.__CEP
    
    #Definindo os métodos set, pois os atributos foram declarados como privados:
    def setCliente(self, cli):
      self.__Cliente = cli
    def setPedido(self, p):
      self.__Pedido =  p
    def setQuantidade(self, quant):
      self.__Quantidade = quant
    def setValor(self, val):
      self.__Valor = val
    def setRua(self, rua):
      self._Rua = rua
    def setNumeroCasa(self, n_casa):
      self.__NumeroCasa = n_casa
    def setBairro(self, b):
      self.__Bairro = b
