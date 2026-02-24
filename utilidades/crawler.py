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
    
    # 
