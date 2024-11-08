from entities.misiones import Misiones

class MisionIndividual(Misiones):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool, tipo_de_mision: int):
        super().__init__(nombre, rango, recompensa, completado, tipo_de_mision)


    
