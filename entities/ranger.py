from entities.aventurero import Aventurero
from entities.mascota import Mascota
from exceptions.valorInvalido import ValorInvalido

class Ranger(Aventurero):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mascota: Mascota):
        super().__init__(nombre, ID, puntos_de_habilidad, experiencia, dinero)
        self.__mascota = mascota

    @property
    def mascota(self):
        return self.__mascota
    
    def validar_rango(self, rango_minimo: int):
        puntos = self.puntos_de_habilidad
        if self.puntos_de_habilidad <= 80 and self.mascota != None:
            puntos = puntos + self.mascota.puntos_de_habilidad

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
        
    def __str__(self):
        return super().__str__() + "\n" + str(self.mascota)
        
    def habilidad_total(self):
        if Mascota == None:
            return str(self.puntos_de_habilidad)
        else:
            return str(self.puntos_de_habilidad) + str(self.__mascota.puntos_de_habilidad)