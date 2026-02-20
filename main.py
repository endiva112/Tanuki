from colecciones.mensajes import MENSAJES
import utilidades.utilidades_shell as shellUtils
import utilidades.utilidades_menores as minorUtils

# Esta variable contendrá el dispositivo android o el AVD (android virtual device) que se usará durante la ejecución del programa
dispositivo = ''

print(MENSAJES[0]) #print(MENSAJES[1].format(i=404))

listadoDeDispositivos = shellUtils.listar_dispositivos()
dispositivo = shellUtils.seleccionar_dispositivo(listadoDeDispositivos)

print("Se ha seleccionado -> " + dispositivo)

opcion = minorUtils.mostrarMenuOpciones()

#Posibles excepciones ya controladas en mostrarMenuOpciones()
if opcion == 1:
    shellUtils.instalarDesdeCarpeta(dispositivo)
elif opcion == 2:
    shellUtils.explorarAppYaInstalada(dispositivo)
    print("Opción no implementada aún")
elif opcion == 3:
    shellUtils.desinstalar(dispositivo)
    print("Opción no implementada aún")
