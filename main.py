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
    appSeleccionada = shellUtils.instalarDesdeCarpeta(dispositivo)
    # Si la instalación fue exitosa comenzamos la exploración
    shellUtils.comenzarExploracion(dispositivo, appSeleccionada)
    
elif opcion == 2:
    appSeleccionada = shellUtils.explorarAppYaInstalada(dispositivo)
    shellUtils.comenzarExploracion(dispositivo, appSeleccionada)

elif opcion == 3:
    shellUtils.desinstalar(dispositivo)
    print("Opción no implementada aún")
