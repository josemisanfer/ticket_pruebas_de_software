from InventoryStub import InventarioStub
from UsersTest import UsuarioDummy
from RepoTest import RepositorioFake
from EmailTest import EmailDummy
from unittest.mock import Mock
from Spy import InventarioSpy

email_mock = Mock()
inventario_spy = InventarioSpy()

class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True

#test

service = TicketService(
   inventario_spy,
   RepositorioFake(),
   email_mock
)
#resultado = service.comprar("Ana", 2)
resultado = service.comprar(UsuarioDummy(), 2)
print (resultado)

email_mock.enviar_confirmacion.assert_called_once()
print(inventario_spy.veces_consultado)

service.comprar(UsuarioDummy(), 1)
print(inventario_spy.veces_consultado)