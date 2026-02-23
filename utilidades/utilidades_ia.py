import sys, time
import utilidades.utilidades_shell as sUtils
from colecciones.comandos import COMANDOS
from colecciones.mensajes import MENSAJES


def explorarPermisos(dispositivo, appSeleccionada):
    permisosSinProcesar = sUtils.extraerPermisos(dispositivo, appSeleccionada)
    print(permisosSinProcesar)
    return