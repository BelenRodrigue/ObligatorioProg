from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.ranger import Ranger

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
    
    def registrar_aventurero_en_el_gremio(self, nombre, clase, fuerza, mana, mascota, ID):
        #no es al pedo validar estos datos si ya lo tenemos en las clases madres? 
        #isinstante eso esta bien? 
        if (nombre is None or nombre == "" or clase is None or clase == "" or mascota == None or not isinstance(mascota, bool)):
            raise ValorInvalido("Los datos ingresados no son correctos.")

        for iter_aventurero in self.__aventureros:
            if type(iter_aventurero) is Aventurero and iter_aventurero.ID == ID:
                raise ValorInvalido("Aventurero ya esta registrado")

        #esta bien asi escrito guerrero? 
        if clase == "Guerrero":
            nuevo_aventurero = Guerrero(nombre, ID, None, None, None, fuerza)
        elif clase == "Mago":
            nuevo_aventurero = Mago (nombre, ID, None, None, None, mana)
        else:
            nuevo_aventurero = Ranger(nombre, ID, None, None, None, mascota)

        self.__aventureros.append(nuevo_aventurero)


    def registrar_mision(self,nombre, rango, recompensa, completado):
        if (nombre is None or nombre == "" or rango is None or rango == "" or recompensa == None or not isinstance(mascota, bool)):
            raise ValorInvalido("Los datos ingresados no son correctos.")
        
        