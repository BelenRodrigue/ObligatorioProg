from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.ranger import Ranger
from entities.mascota import Mascota

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
    
    def registrar_aventurero_en_el_gremio(self, nombre: str, clase: str,  puntos_de_habilidad:  int, experiencia: int, dinero: float, fuerza: int, mana: int, mascota: bool, nombre_mascota: str, ptos_habilidad_mascota: int, ID: int):
     
        for iter_aventurero in self.__aventureros:
            if type(iter_aventurero) is Aventurero and iter_aventurero.ID == ID:
                raise ValorInvalido("Aventurero ya esta registrado")

        if clase == "Guerrero":
            nuevo_aventurero = Guerrero(nombre, ID, puntos_de_habilidad, experiencia, dinero, fuerza)
        elif clase == "Mago":
            nuevo_aventurero = Mago (nombre, ID, puntos_de_habilidad, experiencia, dinero, mana)
        else:
            if mascota:
                nueva_mascota = Mascota(nombre_mascota, ptos_habilidad_mascota)
            else:
                nueva_mascota = None
            nuevo_aventurero = Ranger(nombre, ID, puntos_de_habilidad, experiencia, dinero, nueva_mascota)


        self.__aventureros.append(nuevo_aventurero)


    def registrar_mision(self,nombre, rango, recompensa, completado):
        if (nombre is None or nombre == "" or rango is None or rango == "" or recompensa == None or not isinstance(mascota, bool)):
            raise ValorInvalido("Los datos ingresados no son correctos.")
        
        