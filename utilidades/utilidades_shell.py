# Wrapper que permite a python lanzar comandos por terminal
import subprocess, sys
from colecciones.comandos import COMANDOS

def listar_dispositivos():
    try:
        #Ejecuta el comando en CMD
        resultado = subprocess.run(COMANDOS[0], shell=True, capture_output=True, text=True, check=True)

        lineas = resultado.stdout.strip().splitlines()
        dispositivos_raw = lineas[1:]

        # Filtramos y construimos lista de dispositivos
        dispositivos = []
        for d in dispositivos_raw:
            if d.strip() != "":  # línea no vacía
                dispositivos.append(d.strip())

        # Si no hay dispositivos
        if len(dispositivos) == 0:
            print("No se reconoce ningún dispositivo conectado, prueba a abrir un terminal y ejecutar 'adb devices', \n" \
            "si tampoco ves salida, el problema no se encuentra en este programa, el problema es de adb.\n" \
            "============================================================")
            return []

        # Enumeramos y mostramos
        print("Seleccione uno de los siguientes dispositivos:")
        for idx, disp in enumerate(dispositivos, start=1):
            print(" "f"{idx}) {disp}")
        return dispositivos

    except FileNotFoundError:
        print("ERROR: 'adb' no se encuentra instalado o no está en PATH.")
    sys.exit(1)

def seleccionar_dispositivo(listadoDeDispositivos):
    try:
        numero = int(input("------------\n"
        "Seleccione el dispositivo a usar: "))

        dispositivo_raw = listadoDeDispositivos[numero - 1]
        return dispositivo_raw.split()[0]
    except IndexError:
        print("============================================================\n" \
        "Opción inválida.")
    except ValueError:
        print("============================================================\n" \
        "Solo se permiten números enteros como valor.")
    sys.exit(1)


def ejecutarComando(comando):
    subprocess.run(comando, shell=True)