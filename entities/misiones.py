class Misiones:
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool, tipo_de_mision: int):
        self.__nombre = nombre 
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado 
        self.__tipo_de_mision = tipo_de_mision

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def completado(self):
        return self.__completado
    
    @property
    def tipo_de_mision(self):
        return self.__tipo_de_mision
