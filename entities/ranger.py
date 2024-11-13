from entities.aventurero import Aventurero
from entities.mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mascota: Mascota):
        super().__init__(nombre, ID, puntos_de_habilidad, experiencia, dinero)
        self.__mascota = mascota

    @property
    def mascota(self):
        return self.__mascota
    