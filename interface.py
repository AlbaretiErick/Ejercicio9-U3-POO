from zope.interface import Interface, implementer
from zope.interface.exceptions import Invalid

class PosicionInvalidaException(Exception):
    pass
class IVehiculo(Interface):
    def insertarElemento(elemento, posicion):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass
