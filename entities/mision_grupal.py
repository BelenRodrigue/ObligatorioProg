from entities.misiones import Misiones

class MisionGrupal(Misiones):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool, tipo_de_mision: int, cantidad_minima_de_miembros: int):
        super().__init__(nombre, rango, recompensa, completado, tipo_de_mision)
        self.__cantidad_minima_de_miembros = cantidad_minima_de_miembros

    @property
    def cantidad_minima_de_miembros(self):
        return self.__cantidad_minima_de_miembros
    
