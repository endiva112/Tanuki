# Wrapper que permite a python lanzar comandos por terminal
import subprocess, sys
import utilidades.utilidades_menores as mUtils
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

# Ejecuta un comando de COMANDOS[indice] reemplazando placeholders con kwargs
def ejecutarComando(indice, **kwargs):
    comando_template = COMANDOS[indice]
    comando = comando_template.format(**kwargs)
    print("Ejecutando:", comando)
    
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    return resultado.stdout, resultado.stderr

# Permite instalar fácilmente la apk que hayas seleccionado y explorarla
def instalarDesdeCarpeta(dispositivo):
    apks = mUtils.listar_apks()

    if not apks:
        print("No hay archivos .apk en la carpeta.")
        sys.exit(1)

    print("Seleccione una APK para instalar:\n")

    # Mostrar menú
    for idx, apk in enumerate(apks, start=1):
        print(f"{idx}) {apk.stem}")  
        # .stem muestra el nombre sin extensión

    # Elegir APK
    try:
        numero = int(input("------------\nSeleccione una APK: "))

        if 1 <= numero <= len(apks):
            apk_seleccionada = apks[numero - 1]
        else:
            print("Opción inválida.")
            sys.exit(1)

        stdout, stderr = ejecutarComando(1, dispositivo=dispositivo, apk=apk_seleccionada)

        if stderr:
            print("ERROR:", stderr)
        else:
            print(stdout)

    except ValueError:
        print("Debe introducir un número.")
        sys.exit(1)


def reinstalar(dispositivo):
    return 0

def desinstalar(dispositivo):
    return 0

def explorarAppYaInstalada(dispositivo):
    return 0



