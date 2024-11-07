from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido

class Guerrero(Aventurero):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float, fuerza: int):
        super().__init__(nombre, ID, puntos_de_habilidad, experiencia, dinero)
        if 1 <= fuerza <= 100:
            self.__fuerza = fuerza
        else:
            raise ValorInvalido("La fuerza debe estar entre 1 y 100.")
    
    @property
    def fuerza(self):
        return self.__fuerza
    

