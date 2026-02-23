# Diccionario de mensajes como placeholders

COMANDOS = [
    'adb devices',                                                                                      #0 Listar dispositivos
    'adb -s {dispositivo} install -r -t {apk}',                                                         #1 Instalar o reinstalar apk, incluso las que son test only
    'adb -s {dispositivo} uninstall {apk}',                                                             #2 Desinstalar
    'adb -s {dispositivo} shell pm list packages',                                                      #3 Listar todas las apps
    'adb -s {dispositivo} shell pm list packages -3',                                                   #4 Listar apps instaladas por el usuario
    'adb -s {dispositivo} shell pm list packages -s',                                                   #5 Listar apps del sistema
    'adb -s {dispositivo} shell pm list packages -f',                                                   #6 Mostrar rutas de las apks, no creo que se llegue a usar
    'adb -s {dispositivo} shell cmd package resolve-activity --brief --components {nombre_app}',        #7 Devuelve nombre y activity de una apk, necesario para poder lanzarla
    'adb -s {dispositivo} shell input keyevent 3',                                                      #8 Vuelve al home del teléfono sin importar que app esté abierta
    'adb -s {dispositivo} shell am start -n {apk_y_activity}',                                          #9 Lanza la app seleccionada con la activity seleccionada
    ''
]
