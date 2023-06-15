class Vehiculo:
    def  __init__ (self,modelo,puertas,color,precio):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio_base = precio
    def getprecio (self):
        return int(self.__precio_base)
    def calcular_precio_venta(self):
        pass
class Nuevo(Vehiculo):
    def __init__ (self,modelo,puertas,color,precio,version):
        super().__init__(modelo,puertas,color,precio)
        self.__version = version
    def getversion (self):
        return self.__version
    def toJSON(self):
        d = dict(__class__=self.__class__.__name__, __atributos__=dict(modelo=self.__modelo,puertas=self.__puertas,color=self.__color,precio=self.__precio_base,version=self.__version))
        return d
    def calcular_precio_venta(self):
        precio_venta = self.getprecio() + (self.getprecio() * 0.10)  
        if self.getversion() == "full":
            precio_venta += self.getprecio() * 0.02  
        return precio_venta
class Usado(Vehiculo):
    def __init__ (self,modelo,puertas,color,precio,marca,patente,año,km):
        super().__init__(modelo,puertas,color,precio)
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = km
    def getaño (self):
        return int(self.__año)
    def getkm (self):
        return int(self.__kilometraje)
    def getpatente  (self):
        return self.__patente
    def calcular_precio_venta(self):
        antiguedad = 2023 - self.getaño()  
        descuento = antiguedad * 0.01  
        if self.getkm() > 100000:
            descuento += 0.02  
        precio_venta = self.getprecio() - (self.getprecio() * descuento)
        return precio_venta
    def toJSON(self):
        d = dict(__class__=self.__class__.__name__, __atributos__=dict(modelo=self.__modelo,puertas=self.__puertas,color=self.__color,precio=self.__precio_base,marca=self.__marca,patente=self.__patente,año=self.__año,km=self.__kilometraje))
        return d
    def modificar_precio_base (self,nuevo):
        self.__precio_base = nuevo