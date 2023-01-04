from pedidosBean import PedidosBean
from pedidosDAO import PedidosDAO

#Pedido no Banco de Dados
p = PedidosBean()
p.setCliente('Débora')
p.setPedido('Doritos')
p.setQuantidade(5)
p.setValor(8)
p.setRua('Cachorinho')
p.setNumeroCasa(1)
p.setBairro('Glitter')
p.setCEP(88888888)

pedidos_dao = PedidosDAO()
pedidos_dao.Inserir_Pedido(p)
