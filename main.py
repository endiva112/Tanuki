# main.py arranca el programa. Muestra el menú, lista los dispositivos, el usuario elige uno. Con ese dispositivo crea una instancia de ADB.
# Luego pregunta si quiere instalar una APK nueva o explorar una ya instalada. Una vez que tiene el dispositivo y la app lista, crea 
# una instancia de Crawler y le dice crawler.iniciar().
from colecciones.mensajes import MENSAJES
from dotenv import load_dotenv
import utilidades.agente_ia as AGENTE_IA
import utilidades.utilidades as utils
import utilidades.adb as ADB
import crawler as CRAWLER
import os


utils.bienvenida()
dispositivos = utils.obtenerDispositivos()
utils.listarDispositivos(dispositivos)
dispositivo = utils.seleccionarDispositivo(dispositivos)

# Creada instancia de adb para dispositivo seleccionado
adb = ADB.ADB(dispositivo)

opcion = utils.mostrarMenuOpciones()
#Posibles excepciones ya controladas en mostrarMenuOpciones()
if opcion == 1:                                             # INSTALACIóN
    utils.instalarDesdeCarpeta(adb)

elif opcion == 2:                                           # EXPLORACIóN
    appSeleccionada = utils.explorarAppYaInstalada(adb)
    print(MENSAJES["inputNombreCarpeta"])
    nombre = str(input("Nombre (ej. TestReloj): "))
    carpetaResultados = utils.crearCarpetaSalida(nombre)

    load_dotenv()
    agenteBarato = AGENTE_IA.AgenteIA(os.getenv("AI_API_URL"), os.getenv("AI_API_KEY"), os.getenv("AI_WORSE_MODEL"))
    agenteComptente = AGENTE_IA.AgenteIA(os.getenv("AI_API_URL"), os.getenv("AI_API_KEY"), os.getenv("AI_MODEL"))

    crawler = CRAWLER.Crawler(adb, appSeleccionada, carpetaResultados, agenteBarato, agenteComptente)
    crawler.iniciar()


elif opcion == 3:                                           # DESINSTALACIóN
    #utils.desinstalar(adb)
    print("Opción no implementada aún")