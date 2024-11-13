from entities.misiones import Misiones

class MisionGrupal(Misiones):
    def __init__(self, nombre: str, rango: int, recompensa: float, cantidad_minima_de_miembros: int):
        super().__init__(nombre, rango, recompensa)
        self.__cantidad_minima_de_miembros = cantidad_minima_de_miembros

    @property
    def cantidad_minima_de_miembros(self):
        return self.__cantidad_minima_de_miembros
    
    def __str__(self):
        return super().__str__() + "\nCantidad de miembros: " + self.cantidad_minima_de_miembros
