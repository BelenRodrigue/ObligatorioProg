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
    
    @property
    def misiones_completadas (self):
        return self.__misiones_completadas
    
    @misiones_completadas.setter
    def incrementar_misiones(self):
        self.misiones_completadas += 1


    def validar_rango(self, rango_minimo: int):
        puntos = self.puntos_de_habilidad + (self.fuerza / 2)

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
            raise ValorInvalido("El rango es inválido")
        
    def habilidad_total(self):
        return self.__puntos_de_habilidad + (self.__fuerza / 2)

    def __str__(self):
        return super.__str__ + "\nFuerza: " + self.fuerza