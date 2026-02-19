from colecciones.mensajes import MENSAJES
import utilidades.utilidades_shell as utils

# Esta variable contendrá el dispositivo android o el AVD (android virtual device) que se usará durante la ejecución del programa
dispositivo = ''

print(MENSAJES[0])
#print(MENSAJES[1].format(i=404))

listadoDeDispositivos = utils.listar_dispositivos()
dispositivo = utils.seleccionar_dispositivo(listadoDeDispositivos)

print(dispositivo)