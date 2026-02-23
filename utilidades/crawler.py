import subprocess, sys
import utilidades.utilidades_shell as sUtils
from colecciones.comandos import COMANDOS
from colecciones.mensajes import MENSAJES

# Este es el método principal de DFS del programa
def iniciarInvestigacion(dispositivo, appSeleccionada, carpetaResultados):

    # Lo primero es cerrar (salir de) cualquier app abierta
    sUtils.restablecerFoco(dispositivo)

    # Lanza la app seleccionada
    sUtils.ejecutarComando(9, dispositivo=dispositivo, apk_y_activity=appSeleccionada)
    print("done")

    archivo = carpetaResultados / "itWorks.txt"
    with open(archivo, "w") as f:
        f.write("Hola mundo")
    
