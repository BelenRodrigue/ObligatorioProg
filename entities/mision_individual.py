from entities.misiones import Misiones

class MisionIndividual(Misiones):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool):
        super().__init__(nombre, rango, recompensa, completado)


    
