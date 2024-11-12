from entities.aventurero import Aventurero

class Ranger(Aventurero):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mascota: bool):
        super().__init__(nombre, ID, puntos_de_habilidad, experiencia, dinero)
        self.__mascota = mascota 
        #validar bool con insistance? (sino como?)

    @property
    def mascota(self):
        return self.__mascota
    
    