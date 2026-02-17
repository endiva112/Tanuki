from adb_utils import list_devices

def main():
    devices = list_devices()
    if not devices:
        print("No hay dispositivos conectados.")
        return

    print("Dispositivos conectados:")
    for i, d in enumerate(devices):
        print(f"{i+1}. {d}")

if __name__ == "__main__":
    main()
