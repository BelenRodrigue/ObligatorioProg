from entities.gremio import Gremio
from entities.ranger import Ranger
from entities.mago import Mago
from entities.guerrero import Guerrero
from exceptions.valorInvalido import ValorInvalido

def mostrar_menu_principal():
    print("Bienvenido al Simulador de Gremio de Aventureros! \n")
    print("Seleccione una opción")
    print("1. Registrar Aventurero")
    print("2. Registrar Misión")
    print("3. Realizar Misión")
    print("4. Otras Consultas")
    print("5. Salir")

def registrar_aventurero(gremio: Gremio):
    print("Elija la clase del aventurero:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Ranger")

    tiene_mascota = None
    mana = None
    fuerza = None
    nombre_mascota = None
    habilidad_mascota = None

    option = int(input())

    if option == 1:
        clase = "Guerrero"
    elif option == 2:
        clase = "Mago"
    elif option == 3:
        clase = "Ranger"
    else:
        # poner un raise 
        print("Error")

    print("Ingrese el nombre:")
    nombre = str(input())
    print("Ingrese el ID:")
    id = int(input())
    print("Ingrese los puntos de habilidad:")
    puntos_habilidad = int(input())
    print("Ingrese la experiencia:")
    experiencia = int(input())
    print("Ingrese el dinero:")
    dinero = float(input())
    
    if clase == "Guerrero":
        print("Ingrese la fuerza del Guerrero:")
        fuerza = int(input())
    elif clase == "Mago":
        print("Ingrese la mana del Mago:")
        mana = int(input())
    else:
        print("Ingrese si el Ranger tiene mascota (S/N):")
        tiene_mascota = str(input())
        if tiene_mascota == "S":
            print("Ingrese nombre de la mascota:")
            nombre_mascota = str(input())
            print("Ingrese los puntos de habilidad de la mascota:")
            habilidad_mascota = int(input())
    
    if tiene_mascota == "S": 
        tiene_mascota_bool = True 
    else: 
        tiene_mascota_bool = False

    gremio.registrar_aventurero_en_el_gremio(nombre, clase, puntos_habilidad, experiencia, dinero, fuerza, mana, tiene_mascota_bool, nombre_mascota, habilidad_mascota, id)

def registrar_mision(gremio: Gremio):
    cantidad_miembros = 0
    print("Ingrese el nombre de la misión:")
    nombre = str(input())
    print("Ingrese el rango de la misión:")
    rango = int(input())
    print("Ingrese la recompensa de la misión:")
    recompensa = float(input())
    print("Es misión grupal? (S/N):")
    grupal = str(input())
    if grupal == "S":
        print("Ingrese la cantidad minima de miembros para la misión:")
        cantidad_miembros = int(input())

    gremio.registrar_mision(nombre, rango, recompensa, cantidad_miembros)

def realizar_mision(gremio: Gremio):
    print("Ingrese el nombre de la misión:")
    nombre = str(input())

    ids = []
    pedir_mas = "S"
    while(pedir_mas == "S"):
        print("Ingrese el ID del aventurero:")
        id = int(input())
        ids.append(id)
        print("Agregar otro aventurero a la misión? (S/N):")
        pedir_mas = str(input())

    gremio.realizar_mision(ids, nombre)

def otras_consultas(gremio: Gremio):
    print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
    print("2. Ver Top 10 Aventureros con Mayor Habilidad")
    print("3. Ver Top 5 Misiones con Mayor Recompensa")
    print("4. Volver al Menú Principal")
    option = int(input())
    
    if option == 1:
        # Top 10 aventureros con mas misiones resueltas
        gremio.ver_top_10_aventureros_misiones_resueltas()
    elif option == 2:
        # Top 10 aventureros con mayor habilidad
        gremio.ver_top_10_aventureros_por_mayor_habilidad()
    elif option == 3:
        # Top 5 misiones con mayor recompensa
        gremio.ver_top_5_misiones_con_mayor_recompensa()


if __name__ == '__main__':
    gremio = Gremio()
    the_end = False

    # Inserts de ayuda
    gremio.registrar_aventurero_en_el_gremio("aa", "Guerrero", 1, 1, 1.0, 1, None, False, None, None, 1)
    gremio.registrar_aventurero_en_el_gremio("bb", "Mago", 1, 1, 1.0, None, 2, False, None, None, 2)
    gremio.registrar_aventurero_en_el_gremio("cc", "Ranger", 1, 1, 1.0, None, None, True, "aki", 10, 3)
    gremio.registrar_mision("mision", 1, 2.0, 1)
    # 

    while(the_end == False):
        # Prints de ayuda
        # print()
        # print("############")
        # print(gremio)
        # print("############")
        # print()
        # 

        mostrar_menu_principal()
        try:
            option = int(input())
            if option == 1:
                # Registrar aventurero
                registrar_aventurero(gremio)
            elif option == 2:
                # Registrar misión
                registrar_mision(gremio)
            elif option == 3:
                # Realizar misión
                realizar_mision(gremio)
            elif option == 4:
                # 
                otras_consultas(gremio)
            elif option == 5:
                # Finalizar la simulacion
                the_end = True
        except ValorInvalido as ex:
            print(ex.mensaje)
        # Descomentar antes de entregar 
        # except:
        #     print("Error de ingreso de datos")