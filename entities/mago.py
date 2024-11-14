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
    
    def validar_rango(self, rango_minimo: int):
        puntos = self.puntos_de_habilidad + round(self.mana / 10)

        if 1 <= puntos <= 20:
            rango = 1
        elif 21 <= puntos <= 40:
            rango = 2
        elif 41 <= puntos <= 60:
            rango = 3
        elif 61 <= puntos <= 80:
            rango = 4
        else:
            rango = 5

        if rango < rango_minimo:
            raise ValorInvalido ("El rango es inválido")
        
    def habilidad_total(self):
        return self.puntos_de_habilidad + round(self.__mana / 10)
    
    def __str__(self):
        return super().__str__() + "\nMana: " + str(self.mana)