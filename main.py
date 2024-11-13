from entities.ranger import Ranger

def mostrar_menu_principal():
    print("Bienvenido al Simulador de Gremio de Aventureros! \n")
    print("Seleccione una opción")
    print("1. Registrar Aventurero")
    print("2. Registrar Misión")
    print("3. Realizar Misión")
    print("4. Otras Consultas")
    print("5. Salir")

def registrar_aventurero():
    print("Elija la clase del aventurero:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Ranger")

    option = int(input())

    if option == 1:
        clase = "Guerrero"
    elif option == 2:
        clase = "Mago"
    elif option == 3:
        clase = "Ranger"
    else: 
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

def registrar_mision():
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

def realizar_mision():
    print("Ingrese el nombre de la misión:")
    nombre = str(input())

    pedir_mas = "S"
    while(pedir_mas == "S"):
        print("Ingrese el ID del aventurero:")
        id = int(input())
        print("Registrar otro aventurero? (S/N):")
        pedir_mas = str(input())

def otras_consultas():
    print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
    print("2. Ver Top 10 Aventureros con Mayor Habilidad")
    print("3. Ver Top 5 Misiones con Mayor Recompensa")
    print("5. Volver al Menú Principal")
    option = int(input())
    
    if option == 1:
        # Top 10 aventureros con mas misiones resueltas
        pass
    elif option == 2:
        # Top 10 aventureros con mayor habilidad
        pass
    elif option == 3:
        # Top 5 misiones con mayor recompensa
        pass


if __name__ == '__main__':

    the_end = False

    while(the_end == False):
        mostrar_menu_principal()
        try:
            option = int(input())

            if option == 1:
                # Registrar aventurero
                registrar_aventurero()
            elif option == 2:
                # Registrar misión
                registrar_mision()
            elif option == 3:
                # Realizar misión
                realizar_mision()
            elif option == 4:
                # 
                otras_consultas()
            elif option == 5:
                # Finalizar la simulacion
                the_end = True
            else:
                # Opcion no valida volver al menu principal
                print(option)
        except:
            print("Error de ingreso de datos")