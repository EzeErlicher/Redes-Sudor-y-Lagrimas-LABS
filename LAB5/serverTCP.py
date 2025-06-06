import socket
import struct
import time
from datetime import datetime
import sys
from cryptography.fernet import Fernet

# Escucha en todas las interfaces locales
HOST = '0.0.0.0'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
totalPackets = 100    # Cantidad de paquetes a transmitir
sleepTime = 1         # Espera en segundos entre el envío de un paquete y el siguiente

# Crea el socket TCP por IPv4 y lo asocia a la dirección especificada
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)  # Escucha solicitudes de conexión con máximo 1 esperando en cola

print(f"Servidor escuchando en {HOST}:{PORT}")

# Activar encriptación si se pasa el argumento -e
encrypt = "-e" in sys.argv
if encrypt:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print(f" Encriptación activada! Compartí esta clave con el cliente: '{key.decode()}'")

connectionSocket, addr = serverSocket.accept()
print(f"  Cliente conectado en {addr[0]}:{addr[1]}")

# Si se pasa el argumento -l, crea el archivo de logueo
logToFile = "-l" in sys.argv
if logToFile:
    filename = "serverTCPLog_encrypted.txt" if encrypt else "serverTCPLog.txt"
    filePath = f"logs/{filename}"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"  Log de ejecución guardado en archivo '{filePath}'")


for i in range(1, totalPackets + 1):
    tx_message = f"{groupName} - {i}"
    tx_bytes = fernet.encrypt(tx_message.encode()) if encrypt else tx_message.encode()

    # El paquete incluye un header de 4 bytes que indica el largo del mensaje para detectar correctamente el límite entre uno y otro
    packet = struct.pack('!I', len(tx_bytes)) + tx_bytes

    try:
        connectionSocket.sendall(packet)
    except (ConnectionAbortedError, ConnectionResetError):
        print("  ERROR: El cliente cerró la conexión.")
        break

    logMessage = f"Mensaje {i} enviado - '{tx_message}' - {datetime.now()}\n"
    if logToFile:
        logFile.write(logMessage)
    else:
        print(logMessage.strip())

    time.sleep(sleepTime)

print(f"  {i} paquetes enviados con éxito al cliente.\nCerrando servidor...")
if logFile: logFile.close()
connectionSocket.close()
