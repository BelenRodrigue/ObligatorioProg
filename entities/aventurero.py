from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float):
        super().__init__()
        self.__nombre = nombre
        self.__ID = ID
        self.__puntos_de_habilidad = puntos_de_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero

    #definimos getters
    @property
    def nombre (self):
        return self.__nombre 

    @property
    def ID (self):
        return self.__ID

    @property
    def puntos_de_habilidad (self):
        return self.__puntos_de_habilidad

    @property
    def experiencia (self):
        return self.__experiencia

    @property
    def dinero (self):
        return self.__dinero

    #definimos setters:
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
         
    #esto  no se si va pero me faltaba un metodo abstracto???:
    @abstractmethod
    def realizar_mision(self):
        pass


