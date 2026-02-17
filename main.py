from adb_utils import listar_dispositivos, ejecutar_comando_adb

def main():
    dispositivos = listar_dispositivos()

    if not dispositivos:
        print("No hay dispositivos conectados.")
        return

    print("Dispositivos conectados:")
    for i, dispositivo in enumerate(dispositivos):
        print(f"{i+1}. {dispositivo}")

    opcion = input("Elige un dispositivo por número: ")

    try:
        indice = int(opcion) - 1
        dispositivo_elegido = dispositivos[indice]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return

    print("Has elegido:", dispositivo_elegido)

    ## lanzar una app. TODO -> AGREGAR SISTEMA POR EL CUAL PODER ELEGIR QUE APP LANZAR

    paquete = "com.google.android.deskclock/com.android.deskclock.DeskClock"

    comando = [
        "adb",
        "-s",
        dispositivo_elegido,
        "shell",
        "am",
        "start",
        "-n",
        paquete
    ]

    salida = ejecutar_comando_adb(comando)
    print(salida)

# Este trocito es esencial y el final del main
if __name__ == "__main__":
    main()

