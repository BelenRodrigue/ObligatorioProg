from abc import ABC, abstractmethod
from exceptions.valorInvalido import ValorInvalido

class Aventurero(ABC):
    def __init__(self, nombre: str, ID: int, puntos_de_habilidad: int, experiencia: int, dinero: float):
        super().__init__()
        if nombre == None or nombre == "":
            raise ValorInvalido("El nombre esta incorrecto")

        if ID == None or ID <= 0:
            raise ValorInvalido("El ID esta incorrecto")
        
        if experiencia == None or experiencia <= 0:
            raise ValorInvalido("La experiencia esta incorrecta")
        
        if dinero == None or dinero <= 0:
            raise ValorInvalido("El dinero está incorrecto")
        
        if 1 <= puntos_de_habilidad <= 100:
            self.__puntos_de_habilidad = puntos_de_habilidad
        else:
            raise ValorInvalido("Los puntos de habilidad deben estar entre 1 y 100.")
        
        self.__nombre = nombre
        self.__ID = ID
        self.__experiencia = experiencia
        self.__dinero = dinero
        self.__misiones_completadas = 0

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

    @property
    def misiones_completadas (self):
        return self.__misiones_completadas

    #definimos setters:
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre   

    @misiones_completadas.setter
    def incrementar_misiones(self):
        self.misiones_completadas += 1

    @abstractmethod
    def validar_rango(self, rango_minimo: int):
        pass

    @abstractmethod
    def habilidad_total(self) -> int:
        pass

    def __str__(self):
        return "Nombre: " + self.nombre + "\nPuntos de habilidad: " + str(self.puntos_de_habilidad) + "\nExperiencia: " + str(self.experiencia) + "\nDinero: " + str(self.dinero)