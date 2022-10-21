# poo
creación de una interfaz de tres sistemas creadas para un restaurante

class roducto:
    
    #Constructor
    def __init__(self,nombre='Sin Nombre',precio=0.0):        
        #Atributos
        self.__Nombre = nombre
        self.__Precio = precio
        
        
    #Métodos -> Funcionalidades: Comportamiento
    def calcularPrecioSinIva(self):
        precioSinIva = self.__Precio - (self.__Precio * 0.19)
        return precioSinIva
    
    def mostrarConsola(self):
        print("------- Info Producto--------")
        print("Nombre: ",self.__Nombre)
        print("Precio: ",self.__Precio)
        print("-----------------------------")
    
    #Getters
    def getNombre(self):
        return self.__Nombre
    
    def getPrecio(self):
        return self.__Precio
    
    #Setters
    def setNombre(self, nuevoNombre):
        self.__Nombre = nuevoNombre
        
    def setPrecio(self, nuevoPrecio):
        self.__Precio = nuevoPrecio
