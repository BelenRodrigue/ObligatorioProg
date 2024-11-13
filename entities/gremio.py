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
    def __init__(self):
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


    def registrar_mision(self, nombre: str, rango: int, recompensa: float, cantidad_miembros: int):
        if cantidad_miembros > 0:
            nueva_mision = MisionGrupal(nombre, rango, recompensa, cantidad_miembros)
        else:
            nueva_mision = MisionIndividual(nombre, rango, recompensa)

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
        #falta terminar 

    def ver_top_10_aventureros_misiones_resueltas(self, aventureros):
        aventureros_ordenados = self.__aventureros
        aventureros_ordenados.sort(key= lambda aventurero: (-aventurero.misiones_completadas, aventurero.nombre)) 

        n = 0
        while (n < 10 and n < len(aventureros_ordenados)):
            print(str(n+1))
            print(aventureros_ordenados[n])
            n += 1

    def ver_top_10_aventureros_por_mayor_habilidad(self):        
        aventureros_ordenados = self.__aventureros
        aventureros_ordenados.sort(key= lambda aventurero: (-aventurero.habilidad_total(), -aventurero.experiencia)) 
        
        n = 0
        while (n < 10 and n < len(aventureros_ordenados)):
            print(str(n+1))
            print(aventureros_ordenados[n])
            n += 1

    def ver_top_5_misiones_con_mayor_recompensa(self):
        misiones_ordenadas = self.__misiones
        misiones_ordenadas.sort(key= lambda mision: (-mision.recompensa, mision.nombre)) 

        n = 0
        while (n < 5 and n < len(misiones_ordenadas)):
            print(str(n+1))
            print(misiones_ordenadas[n])
            n += 1

    def __str__(self):
        aventureros = ""
        for aventu_iter in self.aventureros:
            aventureros = aventureros + aventu_iter.__str__()
        
        misiones = ""
        for mision_iter in self.misiones:
            misiones = misiones + mision_iter.__str__()

        return aventureros









