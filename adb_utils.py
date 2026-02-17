import subprocess

#Esto nos permitirá listar dispositivos conectados
def run_adb_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

def list_devices():
    output = run_adb_command(["adb", "devices"])
    devices = []
    for line in output.splitlines()[1:]:
        if "device" in line:
            devices.append(line.split()[0])
    return devices
