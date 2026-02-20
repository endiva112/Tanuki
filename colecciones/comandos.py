# Diccionario de mensajes como placeholders

COMANDOS = [
    'adb devices',                                  #Listar dispositivos
    'adb -s {dispositivo} install -t {apk}',        #Instalar apk, incluso las que son test only
    'adb -s {dispositivo} install -r -t {apk}',     #Reinstalar
    'adb -s {dispositivo} uninstall {apk}',         #Desinstalar
    'adb shell pm list packages',                   #Listar todas las apps
    'adb shell pm list packages -3',                #Listar apps instaladas por el usuario
    'adb shell pm list packages -s',                #Listar apps del sistema
    'adb shell pm list packages -f'                 #Mostrar rutas de las apks, no creo que se llegue a usar
]
