# crawler.py toma el control. Vuelve al home del teléfono, lanza la app, y entra en su bucle principal. En cada iteración hace siempre lo mismo: 
# toma captura de pantalla, descarga el XML, parsea el XML con parser_ui.py para obtener un JSON limpio de elementos interactivos, se lo pasa 
# junto con la captura a cliente_ia.py, y la IA le devuelve qué elementos son y qué representan funcionalmente. 
# Con eso decide qué acción ejecutar a continuación usando adb.py, y actualiza el grafo. 
# Repite hasta que no quedan acciones nuevas por explorar o hasta que el usuario lo para.
from colecciones.mensajes import MENSAJES
import time, sys

class Crawler:
    # Constructor
    def __init__(self, adb, appSeleccionada, carpetaResultados, basicAI, competentAI):
        self.adb = adb
        self.appSeleccionada = appSeleccionada
        self.carpetaResultados = carpetaResultados
        self.basicAI = basicAI
        self.competentAI = competentAI

    # Métodos auxiliares
    def hacerCapturaPantalla(self, id):
        self.adb.hacerCapturaPantalla()
        self.adb.descargarCapturaPantalla(self.carpetaResultados/"capturas", id)
        time.sleep(0.2)

    # Extrae los permisos, los procesa y lso guarda en el formato correcto
    def extraerPermisos(self):
        print(MENSAJES["infoExtrayendoPermisos"])

        partes = self.appSeleccionada.split("/")
        appSinActivity = partes[0]
        
        # Obtenemos permisos sin procesar
        stdout, stderr = self.adb.extraerPermisosAPP(appSinActivity)
        permisosRAW = stdout

        if stderr:
            print("(ERROR) ", stderr)
            sys.exit(1)

        # Abrir y leer un archivo completo
        with open("prompts/PERMISOS.txt", "r", encoding="utf-8") as f:
            prompt = f.read()
        
        # Preparamos el cuerpo de nuestra petición
        peticion = prompt + permisosRAW
        
        # Consultamos a la API
        respuestaIA = self.basicAI.atacarAPI(peticion)
        return respuestaIA



    # Método principal de la lógica del programa
    def iniciar(self):
        print(MENSAJES["infoComenzandoExploracion"])

        self.adb.pulsarHOME() # Primero salimos al Home
        time.sleep(0.1)

        idImg = 0 # lo ideal es que la app pueda ir generando un id unico para cada vista, pero eso es un problema para el futuro TODO

        # Empezamos la navegación desde feura de la app
        self.hacerCapturaPantalla(idImg)

        # Lanzamos la app
        self.adb.lanzarAPP(self.appSeleccionada)
        exploracionTerminada = False

        # Generamos informe de permisos
        respuestaIA = self.extraerPermisos()
        print(MENSAJES["exitoExtracciónPermisos"])

        informePermisos = self.carpetaResultados / "Informe_de_permisos.txt"
        with open(informePermisos, "w", encoding="utf-8") as f:
            f.write(respuestaIA)

        while exploracionTerminada == False:
            idImg += 1
            self.hacerCapturaPantalla(idImg)
            print("el bucle funciona")
            time.sleep(0.5)
            if idImg == 3:
                exploracionTerminada = True

        print("Análisis del crawler finalizado")