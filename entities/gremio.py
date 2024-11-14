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
        print("Aventurero registrado con exito")


    def registrar_mision(self, nombre: str, rango: int, recompensa: float, cantidad_miembros: int):
        if cantidad_miembros > 0:
            nueva_mision = MisionGrupal(nombre, rango, recompensa, cantidad_miembros)
        else:
            nueva_mision = MisionIndividual(nombre, rango, recompensa)

        self.__misiones.append(nueva_mision)
        print("Misión registrada con exito")

    def realizar_mision (self, ids: list, nombre_mision: str):

        # Buscamos y validamos la mision
        mision = None
        index = -1
        for mision_iter in self.__misiones:
            index += 1
            if mision_iter.nombre == nombre_mision:
                mision = mision_iter
        if mision == None:
            raise ValorInvalido("No se encontro una misión con ese nombre")
        if mision.completado == True:
            raise ValorInvalido("La misión ya esta completada")

        mision.reset_aventureros()
        # Validamos que todos los ids sean de aventureros en el gremio y validamos sus rangos

        aventureros_nuevo = []
        recompensa_individual = mision.recompensa / len(self.__aventureros)
        if mision.rango == 1:
            recompensa_experiencia = 5
        elif mision.rango == 2:
            recompensa_experiencia= 10 
        elif mision.rango == 3:
            recompensa_experiencia= 20
        elif mision.rango == 4:
            recompensa_experiencia = 50
        else:
            recompensa_experiencia= 100 

        for id_iter in ids:
            encontre = False
            for aventurero_iter in self.__aventureros:
                if aventurero_iter.ID == id_iter:
                    encontre = True
                    aventurero_iter.validar_rango(mision.rango)
                    mision.set_aventureros(aventurero_iter) 
                    aventurero_iter.add_dinero(recompensa_individual)
                    aventurero_iter.add_experiencia(recompensa_experiencia)
                    aventurero_iter.incrementar_misiones()
                    aventureros_nuevo.append(aventurero_iter)
                    print("Misión Existosa")
                else:
                    print("Misión Fallida")
            if encontre == False:
                raise ValorInvalido("No se encontro el aventurero en el gremio")
            
        del self.__misiones[index]
        mision.set_completado()
        self.__misiones.append(mision)
        self.__aventureros = aventureros_nuevo

    def ver_top_10_aventureros_misiones_resueltas(self):
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
            aventureros = aventureros + "\n" + str(aventu_iter)
        
        misiones = ""
        for mision_iter in self.misiones:
            misiones = misiones + "\n"  + str(mision_iter)

        return aventureros + "\n" + misiones









