import subprocess

#Esto nos permitirá listar dispositivos conectados
def ejecutar_comando_adb(comando):
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout.strip()

def listar_dispositivos():
    salida = ejecutar_comando_adb(["adb", "devices"])
    dispositivos = []
    for linea in salida.splitlines()[1:]:  # saltamos la primera línea
        if "device" in linea:
            dispositivos.append(linea.split()[0])
    return dispositivos
