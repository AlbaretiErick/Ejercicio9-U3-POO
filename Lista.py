from clsVehiculo import Vehiculo,Nuevo,Usado
from interface import IVehiculo,ITesorero,IDirector
from interface import PosicionInvalidaException
from zope.interface import Interface, implementer
from zope.interface.exceptions import Invalid
import json
from pathlib import Path
@implementer(IVehiculo)
class Nodo:
    __vehiculo: object
    __siguiente: object
    def __init__(self,vehiculo):
        self.__vehiculo = vehiculo
        self.__siguiente = None
    def setsiguiente (self,siguiente):
        self.__siguiente = siguiente
    def getsiguiente (self):
        return self.__siguiente
    def getdato (self):
        return self.__vehiculo
class Manejador_vehiculos:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > self.__actual:
            raise PosicionInvalidaException("Posición inválida")

        if posicion == 0:
            self.__comienzo = Nodo(elemento, self.__comienzo)
        else:
            nodo_actual = self.__comienzo
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.getsiguiente()
            nuevo_nodo = Nodo(elemento, nodo_actual.getsiguiente())
            nodo_actual.setsiguiente(nuevo_nodo)
        self.__actual += 1
    def agregarElemento(self, elemento):
        self.insertarElemento(elemento, self.__actual)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= self.__actual:
            raise PosicionInvalidaException("Posición inválida")

        nodo_actual = self.__comienzo
        for _ in range(posicion):
            nodo_actual = nodo_actual.getsiguiente()
        return nodo_actual.getdato()   
    def agregar_vehiculo (self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        
    def modificar_precio_base_por_patente(self, patente):
        nodo_actual = self.__comienzo
        while nodo_actual:
            vehiculo = nodo_actual.getdato()
            if isinstance(vehiculo, Usado) and vehiculo.getpatente() == patente:
                nuevo = input ("ingresar nuevo precio: \n")
                vehiculo.modificar_precio_base(nuevo)
                nuevo_precio_venta = vehiculo.calcular_precio_venta()
                print(f"El nuevo precio de venta del vehículo con patente '{patente}' es: {nuevo_precio_venta:.2f}")
                return
            nodo_actual = nodo_actual.siguiente

        print(f"No se encontró ningún vehículo usado con la patente '{patente}'.")
    def mostrar_vehiculo_mas_economico(self):
        vehiculo_mas_economico = None
        nodo_actual = self.__comienzo
        while nodo_actual:
            vehiculo = nodo_actual.getdato()
            if vehiculo_mas_economico is None or vehiculo.calcular_precio_venta() < vehiculo_mas_economico.calcular_precio_venta():
                vehiculo_mas_economico = vehiculo

        if vehiculo_mas_economico is None:
            print("No hay vehículos en la lista.")
        else:
            print("Datos del vehículo más económico:")
            print("Modelo:", vehiculo_mas_economico.getmodelo())
            print("Cantidad de puertas:", vehiculo_mas_economico.getpuertas())
            print("Color:", vehiculo_mas_economico.getcolor())
            print("Precio base:", vehiculo_mas_economico.getprecio())
            print("Importe de venta:", vehiculo_mas_economico.calcular_precio_venta())
    def mostrar_datos_vehiculos(self):
        nodo_actual = self.__comienzo
        while nodo_actual is not None:
            vehiculo = nodo_actual.dato
            print("Modelo:", vehiculo.getmodelo())
            print("Cantidad de puertas:", vehiculo.getpuertas())
            print("Importe de venta:", vehiculo.calcular_precio_venta())
            print()
    def cargar_vehiculos_desde_json(self):
        with open("vehiculos.json") as archivo:
            datos = json.load(archivo)
        for vehiculo_data in datos:
            if vehiculo_data['tipo'] == 'Nuevo':
                vehiculo = Nuevo(
                    vehiculo_data['modelo'],
                    vehiculo_data['puertas'],
                    vehiculo_data['color'],
                    vehiculo_data['precio_base'],
                    vehiculo_data['version']
                )
            else:
                vehiculo = Usado(
                    vehiculo_data['modelo'],
                    vehiculo_data['puertas'],
                    vehiculo_data['color'],
                    vehiculo_data['precio_base'],
                    vehiculo_data['marca'],
                    vehiculo_data['patente'],
                    vehiculo_data['año'],
                    vehiculo_data['kilometraje']
                )

            self.agregarElemento(vehiculo)
    def guardar_en_archivo(self,):
        vehiculos = []
        for vehiculo in self:
            vehiculos.append(vehiculo.toJSON())

        with open('vehiculos.json', "w") as archivo:
            json.dump(vehiculos, archivo)
class Tesorero:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def autenticar(self, username, password):
        return self.__username == username and self.__password == password

    def gastosSueldoPorEmpleado(self, dni):
        # Implementa la lógica para calcular los gastos de sueldo para el empleado con el DNI dado
        pass

class Director:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def autenticar(self, username, password):
        return self.__username == username and self.__password == password

    def modificarBasico(self, dni, nuevoBasico):
        # Implementa la lógica para modificar el sueldo básico del agente con el DNI dado
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        # Implementa la lógica para modificar el porcentaje por cargo para el agente con el DNI dado
        pass

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        # Implementa la lógica para modificar el porcentaje por categoría para el agente con el DNI dado
        pass

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        # Implementa la lógica para modificar el importe extra para el agente con el DNI dado
        pass