import subprocess, sys, time
import utilidades.utilidades_shell as sUtils
import utilidades.utilidades_ia as iaUtils
from colecciones.comandos import COMANDOS
from colecciones.mensajes import MENSAJES

# Este es el método principal de DFS del programa
def iniciarInvestigacion(dispositivo, appSeleccionada, carpetaResultados):

    # Lo primero es cerrar (salir de) cualquier app abierta
    sUtils.restablecerFoco(dispositivo)
    #time.sleep(0.4)

    # Lanza la app seleccionada
    print(MENSAJES[9])
    sUtils.ejecutarComando(9, dispositivo=dispositivo, apk_y_activity=appSeleccionada)

    # Extraer permisos
    print("CONSULTANDO PERMISOS DE LA APLICACIÓN temporalmente deshabilitado mientras se testean otras funcionalidades")
    # resultado = iaUtils.explorarPermisos(dispositivo, appSeleccionada)
    
    # informePermisos = carpetaResultados / "Informe_de_permisos.txt"
    # with open(informePermisos, "w", encoding="utf-8") as f:
    #     f.write(resultado)
    # print("INFORME DE PERMISOS GENERADO descomentar este bloque luego")
    

    # Crear id para la vista
    idVista = 0

    # Tomar captura de pantalla
    time.sleep(0.2)
    sUtils.ejecutarComando(11, dispositivo=dispositivo)
    #Descargar captura de pantalla
    sUtils.ejecutarComando(12, dispositivo=dispositivo, ubicacion=carpetaResultados/"capturas", idImagen=idVista)

    for idVista in range (2):
        # Generar xml
        sUtils.ejecutarComando(13, dispositivo=dispositivo)

        # Descargar xml
        sUtils.ejecutarComando(14, dispositivo=dispositivo, ubicacion=carpetaResultados)

        # Leer el xml
        with open(f"{carpetaResultados}/window_dump.xml", "r", encoding="utf-8") as f:
            miXMLActual = f.read()

        with open("prompts/CASOS_DE_USO.txt", "r", encoding="utf-8") as f:
            prompt = f.read()

        peticion = prompt + miXMLActual
        rutaImagen = f"{carpetaResultados}/capturas/{idVista}.png"
        #print(rutaImagen)
        respuesta = iaUtils.atacarAPI_con_imagen(peticion, rutaImagen)

        informeCasosUso = carpetaResultados / "Informe_de_casos_de_uso.txt"
        with open(informeCasosUso, "a", encoding="utf-8") as f:
            f.write(respuesta)
        
        sys.exit(1)