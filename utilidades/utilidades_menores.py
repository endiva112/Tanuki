# Métodos simples que se han separado del código principal para hacer el proceso de leer el main menos engorroso
import sys

# Devuelve un int correspondiente a la elección del usuario
def mostrarMenuOpciones():
    try:
        print("""
============================================================
                    ¿Qué desea hacer?
============================================================
1) Instalar una APK desde la carpeta de apks
2) Reinstalar una APK desde la carpeta de apks
3) Desinstalar una APK del dispositivo
4) Explorar una aplicación ya instalada en el dispositivo""")
        opcion = int(input("------------\n"
            "Seleccione una opción: "))
        
        if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
            print("============================================================\n" \
            "Opción inválida.")
        else:
            return opcion
    except ValueError:
        print("============================================================\n" \
        "Solo se permiten números enteros como valor.")
    sys.exit(1)