from abc import ABC, abstractmethod
from exceptions.valorInvalido import ValorInvalido 

class Misiones(ABC):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool):
        super().__init__()
        self.__nombre = nombre 
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado 
        self.__aventureros = []

        if self.__nombre == None or self.__nombre == "":
            raise ValorInvalido("El nombre esta incorrecto")

        if self.__recompensa == None or self.__recompensa <= 0:
            raise ValorInvalido("La recompensa esta incorrecta")
        
        if 1 <= rango <= 5:
            self.__rango = rango
        else:
            raise ValorInvalido("El rango debe de estar entre 1 y 5.")


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
    def aventureros(self):
        return self.__aventureros

    @aventureros.setter
    def aventureros(self, nuevo_aventurero):
        self.__aventureros.append(nuevo_aventurero)

    def reset_aventureros(self):
        self.__aventureros = []
