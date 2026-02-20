# Métodos simples que se han separado del código principal para hacer el proceso de leer el main menos engorroso
import sys
from pathlib import Path
from datetime import datetime
from colecciones.mensajes import MENSAJES

# Devuelve un int correspondiente a la elección del usuario
def mostrarMenuOpciones():
    try:
        print(MENSAJES[5])
        opcion = int(input("------------\nSeleccione una opción: "))
        
        if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
            print(MENSAJES[1])
        else:
            return opcion
    except ValueError:
        print(MENSAJES[2])
    sys.exit(1)


# Devuelve un array con todas las apks de la carpeta "apks" de este proyecto
def listarApks():
    base_dir = Path(__file__).resolve().parent  # carpeta utilidades
    proyecto_root = base_dir.parent             # carpeta del Crawler
    carpeta = proyecto_root / "apks"            # Tanuki/apks

    apks = list(carpeta.glob("*.apk"))
    return apks


# Crea la carpeta de output donde se establecerán todos los documentos generados en la exploración
def crearCarpeta(nombre):

    fecha = datetime.now().strftime("%Y%m%d_%H%M%S") # Fecha y hora formateada: 20260220_154210
    carpeta = Path(f"resultados/{nombre}_{fecha}") # Ruta de la carpeta
    carpeta.mkdir(parents=False, exist_ok=False)