from entities.aventurero import Aventurero
from exceptions.valorInvalido import ValorInvalido
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.ranger import Ranger
from entities.mascota import Mascota
from entities.misiones import Misiones
from entities.mision_grupal import MisionGrupal
from entities.mision_individual import MisionIndividual

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


    def registrar_mision(self, nombre, rango, recompensa, completado, cantidad_miembros):
        if cantidad_miembros > 0:
            nueva_mision = MisionGrupal (nombre, rango, recompensa, completado, cantidad_miembros)
        else:
            nueva_mision = MisionIndividual (nombre, rango, recompensa, completado)

        self.__misiones.append(nueva_mision)

    def realizar_mision (self, ids: list, nombre_mision: str):

        # Buscamos y validamos la mision
        mision = None
        index = 0
        for mision_iter in self.__misiones:
            index += 1
            if type(mision_iter) is Misiones and mision_iter.nombre == nombre_mision:
                mision = mision_iter
        if mision == None:
            ValorInvalido("No se encontro una mision con ese nombre")
        if mision.completado == True:
            ValorInvalido("La mision ya esta completada")

        mision.reset_aventureros()
        # Validamos que todos los ids sean de aventureros en el gremio y validamos sus rangos
        for id_iter in ids:
            encontre = False
            for aventurero_iter in self.__aventureros:
                if type(aventurero_iter) is Aventurero and aventurero_iter.ID == id_iter:
                    encontre = True
                    aventurero_iter.validar_rango(mision.rango)
                    mision.aventureros(aventurero_iter)
            if encontre == False:
                raise ValorInvalido("No se encontro el aventurero en el gremio")
            
        del self.__misiones[index]
        mision.completado = True
        self.__misiones.append(mision)
        






