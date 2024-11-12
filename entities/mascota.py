
from exceptions.valorInvalido import ValorInvalido 
class Mascota:
    def __init__(self, nombre: str, puntos_de_habilidad: int):
        if self.__nombre == None or self.__nombre == "":
            raise ValorInvalido("El nombre esta incorrecto")
        if 1 <= puntos_de_habilidad <= 50:
            self.__puntos_de_habilidad = puntos_de_habilidad
        else:
            raise ValorInvalido("Los puntos de hablidad deben estar entre 1 y 50")
   
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def puntos_de_habilidad (self):
        return self.__puntos_de_habilidad
    

