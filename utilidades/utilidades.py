# funciones que gestionan la interacción con el usuario y el sistema de archivos, nada más. Sin ADB, sin IA, sin parseo.
from colecciones.mensajes import MENSAJES
from datetime import datetime
from pathlib import Path
import sys, subprocess

# Saludo
def bienvenida():
    print(MENSAJES["bienvenida"])

# Devuelve un array con los dispositivos que se pueden usar y comprueba si adb está instalado
# Excepción justificada: se ejecuta antes de tener instancia de ADB, las funciones en este archivo nunca deberín ejecutar comandos adb directamente
def obtenerDispositivos():
    try:
        resultado = subprocess.run("adb devices", shell=True, capture_output=True, text=True)

        if resultado.stderr:
            print("(ERROR)", resultado.stderr)
            sys.exit(1)

        lineas = resultado.stdout.strip().splitlines()[1:]
        dispositivos = [linea.split()[0] for linea in lineas if linea.strip()]

        if len(dispositivos) == 0:
            print(MENSAJES["errorSinDispositivos"])
            sys.exit(1)

        return dispositivos
        # TODO - al eliminar la palabra device el programa no distingue entre el dispositivo con y sin permisos y fallara si no se tiene permisos

    except FileNotFoundError:
        print("(ERROR) 'adb' no se encuentra instalado o no está en PATH.")
        sys.exit(1)

# Muestra al usuario que dispositivos puede elegir
def listarDispositivos(misDispositivos):
    print("Estos son los dispositivos que hemos detectado")
    for i, dispositivo in enumerate(misDispositivos, start=1):
        print(f"{i}) {dispositivo}")

# Devuelve el nombre del dispositivo a usar
def seleccionarDispositivo(misDispositivos):
    try:
        numero = int(input("------------\nSeleccione el dispositivo a usar: "))
        return misDispositivos[numero - 1]
    except IndexError:
        print(MENSAJES["errorOpcionInvalida"])
    except ValueError:
        print(MENSAJES["errorNoEsNumero"])
    sys.exit(1)

# Muestra menu de opciones, retorna int de la opción seleccionada por el usuario
def mostrarMenuOpciones():
    try:
        print(MENSAJES["menuPrincipal"])
        opcion = int(input("------------\nSeleccione una opción: "))
        
        if opcion != 1 and opcion != 2 and opcion != 3:
            print(MENSAJES["errorOpcionInvalida"])
        else:
            return opcion
    except ValueError:
        print(MENSAJES["errorNoEsNumero"])
    sys.exit(1)

# Lista las apks en la carpeta de apks
def listarApks():
    base_dir = Path(__file__).resolve().parent  # carpeta utilidades
    proyecto_root = base_dir.parent             # carpeta del Crawler
    carpeta = proyecto_root / "apks"            # Tanuki/apks

    apks = list(carpeta.glob("*.apk"))
    return apks

# Crea la carpeta de output donde se establecerán todos los documentos generados en la exploración y retorna la ruta de dicha carpeta
def crearCarpetaSalida(nombre):
    fecha = datetime.now().strftime("%Y%m%d_%H%M")      # Fecha y hora formateada: 20260220_1542
    carpeta = Path(f"resultados/{nombre}_{fecha}")      # Ruta de la carpeta
    carpeta.mkdir(parents=False, exist_ok=False)

    subcarpeta = carpeta / "capturas"
    subcarpeta.mkdir(parents=False, exist_ok=False)

    return carpeta

# Hace uso de la instancia de adb para permitir lanzar una aplicación
def explorarAppYaInstalada(adb):
    try:
        # Primero se pide que tipo de app listar
        print(MENSAJES["menuListarApps"])
        opcion = int(input("------------\nSeleccione una opción: "))
        
        if opcion == 1:
            stdout, stderr = adb.listarAPPs()
        elif opcion == 2:
            stdout, stderr = adb.listarAPPsUsuario()
        elif opcion == 3:
            stdout, stderr = adb.listarAPPsSistema()
        else:
            # OPción fuera del scope
            print(MENSAJES["errorOpcionInvalida"])
            sys.exit(1)

        # Cazar posibles errores en la ejecución del comando
        if stderr:
            print("(ERROR)", stderr)
            sys.exit(1)

        # Se listan las apps
        print(MENSAJES["infoListandoApps"])
        i = 1

        appsListadas = [linea.replace("package:", "").strip() for linea in stdout.strip().splitlines()]
        for app in appsListadas:
            print(f"{i}) {app}")
            i+=1
        
        indiceAppSeleccionada = int(input("------------\nSeleccione una aplicación para explorar: "))
        appSeleccionada = appsListadas[indiceAppSeleccionada - 1]
        stdout, stderr = adb.obtenerAppActivity(appSeleccionada)
        app_y_activity = stdout
        return app_y_activity

    except IndexError:
        print(MENSAJES["errorOpcionInvalida"])
        sys.exit(1)
    except ValueError:
        print(MENSAJES["errorNoEsNumero"])
        sys.exit(1)

# Instala una apk elegida por el usuario de las presentes en la carpeta APK
def instalarDesdeCarpeta(adb):
    apks = listarApks()

    if not apks:
        print("No hay archivos .apk en la carpeta de APKS.")
        sys.exit(1)

    print(MENSAJES["infoInstalandoAPK"])

    # Mostrar menú
    for idx, apk in enumerate(apks, start=1):
        print(f"{idx}) {apk.stem}")  
        # .stem muestra el nombre sin extensión

    # Elegir APK
    try:
        numero = int(input("------------\nSeleccione una APK: "))

        apk_seleccionada = apks[numero - 1]
        stdout, stderr = adb.instalarAPK(apk_seleccionada)

        if stderr:
            print("(ERROR) ", stderr)
            sys.exit(1)
        else:
            print("(OK) ", stdout)

    except IndexError:
        print(MENSAJES["errorOpcionInvalida"])
        sys.exit(1)
    except ValueError:
        print(MENSAJES["errorNoEsNumero"])
        sys.exit(1)

# 
def desinstalar(adb):
    return 0