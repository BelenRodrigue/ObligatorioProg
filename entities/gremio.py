from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido


class Gremio:
    def __init__(self, aventureros: list, misiones: list):
        self.__aventureros = []
        self.__misiones = []

    @property
    def aventureros(self):
        return self.__aventureros
    
    @property
    def misiones(self):
        return self.__misiones
    
    def registrar_aventurero_en_el_gremio(self, nombre, clase, atributo_adicional, ID):
        
        for iter_aventurero in self.__aventureros:
            if type(iter_aventurero) is Aventurero and iter_aventurero.ID == ID:
                raise ValorInvalido
            
            
