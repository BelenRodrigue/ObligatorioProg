from abc import ABC, abstractmethod
from exceptions.valorInvalido import ValorInvalido 

class Misiones(ABC):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool, tipo_de_mision: int):
        super().__init__()
        self.__nombre = nombre 
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado 
        self.__tipo_de_mision = tipo_de_mision

        if self.__nombre == None or self.__nombre == "":
            raise ValorInvalido("El nombre esta incorrecto")

        if self.__recompensa == None or self.__recompensa <= 0:
            raise ValorInvalido("La recompensa esta incorrecta")
        
        if 1 <= rango <= 5:
            self.__rango = rango
        else:
            raise ValorInvalido("El rango debe de estar entre 1 y 5.")
        
        #dsto no sabemos si esta bien??
        if self.__tipo_de_mision != 1 or self.__tipo_de_mision != 2:
            raise ValorInvalido("El tipo de mision esta incorrecto")
        
        #validar bool con insistance? (sino como?) --> "completado"


    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def completado(self):
        return self.__completado
    
    @property
    def tipo_de_mision(self):
        return self.__tipo_de_mision


    #abstracmethod??