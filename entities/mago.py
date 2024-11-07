from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido

class Mago(Aventurero):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mana: int):
        super().__init__(nombre, ID, puntos_de_habilidad, experiencia, dinero)
        if 1 <= mana <= 1000:
            self.__mana = mana
        else:
            raise ValorInvalido("El mana debe estar entre 1 y 1000.")
    
    @property
    def mana(self):
        return self.__mana
    
