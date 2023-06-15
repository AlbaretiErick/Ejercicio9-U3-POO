from Lista import Manejador_vehiculos
from clsVehiculo import Nuevo
from clsVehiculo import Usado
from clsVehiculo import Vehiculo
class TestListaVehiculos:
    def __init__(self):
        self.lista_vehiculos = Manejador_vehiculos()
    
    def run_tests(self):
        self.test_insertar_vehiculo_en_posicion_0()
        self.test_insertar_vehiculo_en_posicion_intermedia()
        self.test_insertar_vehiculo_en_ultima_posicion()
        self.test_agregar_vehiculo()
        self.test_obtener_objeto_en_posicion()
        self.test_modificar_precio_venta()
    
    def test_insertar_vehiculo_en_posicion_0(self):
        vehiculo = Nuevo("Palio", 4, "Rojo", 15000.0, "Base")
        self.lista_vehiculos.insertarElemento(vehiculo, 0)

    def test_insertar_vehiculo_en_posicion_intermedia(self):
        vehiculo = Usado("Focus", 4, "Negro", 10000.0, "DEF456", 2018, 50000)
        self.lista_vehiculos.insertarElemento(vehiculo, 1)

    def test_insertar_vehiculo_en_ultima_posicion(self):
        vehiculo = Nuevo("Gol", 5, "Azul", 20000.0, "Full")
        self.lista_vehiculos.insertarElemento(vehiculo, len(self.lista_vehiculos))
        
    def test_agregar_vehiculo(self):
        vehiculo1 = Nuevo("Palio", 4, "Rojo", 15000.0, "Base")
        self.lista_vehiculos.agregarElemento(vehiculo1)
        
        vehiculo2 = Usado("Focus", 4, "Negro", 10000.0, "DEF456", 2018, 50000)
        self.lista_vehiculos.agregarElemento(vehiculo2)

        vehiculo3 = Nuevo("Gol", 5, "Azul", 20000.0, "Full")
        self.lista_vehiculos.agregarElemento(vehiculo3)
    def test_obtener_objeto_en_posicion(self):
        vehiculo1 = Nuevo("Palio", 4, "Rojo", 15000.0, "Base")
        self.lista_vehiculos.agregarElemento(vehiculo1)
        
        vehiculo2 = Usado("Focus", 4, "Negro", 10000.0, "DEF456", 2018, 50000)
        self.lista_vehiculos.agregarElemento(vehiculo2)

        vehiculo3 = Nuevo("Gol", 5, "Azul", 20000.0, "Full")
        self.lista_vehiculos.agregarElemento(vehiculo3)
        
        posicion = 1
        vehiculo_obtenido = self.lista_vehiculos.mostrarElemento(posicion)
        
        if vehiculo_obtenido is vehiculo2:
            print("El objeto obtenido en la posición", posicion, "es correcto.")
        else:
            print("Error: El objeto obtenido en la posición", posicion, "no es correcto.")
    def test_modificar_precio_venta(self):
        vehiculo1 = Nuevo("Palio", 4, "Rojo", 15000.0, "Base")
        self.lista_vehiculos.agregarElemento(vehiculo1)
        
        vehiculo2 = Usado("Focus", 4, "Negro", 10000.0, "DEF456", 2018, 50000)
        self.lista_vehiculos.agregarElemento(vehiculo2)

        vehiculo3 = Nuevo("Gol", 5, "Azul", 20000.0, "Full")
        self.lista_vehiculos.agregarElemento(vehiculo3)
        
        patente = "DEF456"
        nuevo_precio_base = 8000.0
        
        for vehiculo in self.lista_vehiculos:
            if isinstance(vehiculo, Usado) and vehiculo.patente == patente:
                vehiculo.precio_base = nuevo_precio_base
                break
        
        for vehiculo in self.lista_vehiculos:
            if vehiculo.patente == patente:
                precio_venta = vehiculo.calcular_precio_venta()
                print("El nuevo precio de venta del vehículo con patente", patente, "es:", precio_venta)
                break
        
        self.verificar_estado_lista()
        
    def verificar_estado_lista(self):
        print("Estado actual de la lista:")
        for vehiculo in self.lista_vehiculos:
            print("Modelo:", vehiculo.getmodelo())
            print("Cantidad de puertas:", vehiculo.getpuertas())
            print("Color:", vehiculo.getcolor())
            print("Precio base:", vehiculo.getprecio())