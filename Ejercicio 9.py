from Lista import Manejador_vehiculos
from clsVehiculo import Vehiculo,Nuevo,Usado
from test import TestListaVehiculos
mn_vehiculos = Manejador_vehiculos()
mn_vehiculos.cargar_vehiculos_desde_json()
test = TestListaVehiculos()
test.run_test()
while True:
        print ("opcion 1:  Insertar un vehículo en la colección en una posición determinada.")
        print ("opcion 2:  Agregar un vehículo a la colección.")
        print ("opcion 3:  Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
        print ("opcion 4:  Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
        print ("opcion 5: mostrar todos los datos del vehiculo mas economico")
        print ("opcion 6: Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
        print ("opcion 7: Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
        print ("opcion 8: salir")
        opcion = input ("ingresar opcion \n")
        if opcion == '1':
            tipo_vehiculo = input("Ingrese el tipo de vehículo (nuevo/usado): \n")
            modelo = input("Ingrese el modelo del vehículo: \n")
            puertas = int(input("Ingrese la cantidad de puertas: \n"))
            color = input("Ingrese el color del vehículo: \n")
            precio_base = float(input("Ingrese el precio base del vehículo: \n"))

            if tipo_vehiculo == "Nuevo":
                version = input("Ingrese la versión del vehículo (base/full): \n")
                vehiculo = Nuevo(modelo, puertas, color, precio_base, version)
            else:
                marca = input("Ingrese la marca del vehículo usado: \n")
                patente = input("Ingrese la patente del vehículo usado: \n")
                año = int(input("Ingrese el año del vehículo usado: \n"))
                kilometraje = float(input("Ingrese el kilometraje del vehículo usado: \n"))
                vehiculo = Usado(modelo, puertas, color, precio_base, marca, patente, año, kilometraje)
            pos = input ('ingresar posicion: \n')
            mn_vehiculos.intertarElemento(pos,vehiculo)
        if opcion == '2':
            tipo_vehiculo = input("Ingrese el tipo de vehículo (nuevo/usado): \n")
            modelo = input("Ingrese el modelo del vehículo: \n")
            puertas = int(input("Ingrese la cantidad de puertas: \n"))
            color = input("Ingrese el color del vehículo: \n")
            precio_base = float(input("Ingrese el precio base del vehículo: \n"))

            if tipo_vehiculo == "nuevo":
                version = input("Ingrese la versión del vehículo (base/full): \n")
                vehiculo = Nuevo(modelo, puertas, color, precio_base, version)
            else:
                marca = input("Ingrese la marca del vehículo usado: \n")
                patente = input("Ingrese la patente del vehículo usado: \n")
                año = int(input("Ingrese el año del vehículo usado: \n"))
                kilometraje = float(input("Ingrese el kilometraje del vehículo usado: \n"))
                vehiculo = Usado(modelo, puertas, color, precio_base, marca, patente, año, kilometraje)
            mn_vehiculos.agregarElemento(vehiculo)
        if opcion == '3':
            pos = input ('ingresar posicion: \n')
            mn_vehiculos.mostrarElemento(pos)
        elif opcion == '4':
            pat = input ('ingresar patente: \n')
            mn_vehiculos.modificar_precio_base_por_patente(pat)
        elif opcion == '5':
            mn_vehiculos.mostrar_vehiculo_mas_economico()
        elif opcion == '6':
            mn_vehiculos.mostrar_datos_vehiculos()
        elif opcion == '7':
            mn_vehiculos.guardar_en_archivo()
        elif opcion == '8':
            break
        else: print ("opcion incorrecta")