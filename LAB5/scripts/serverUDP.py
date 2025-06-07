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

# Crea el socket UDP por IPv4 y lo asocia a la dirección especificada
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((HOST, PORT))
print(f"Servidor UDP escuchando en {HOST}:{PORT}")

# Activar encriptación si se pasa el argumento -e
encrypt = "-e" in sys.argv
if encrypt:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print(f" Encriptación activada! Compartí esta clave con el cliente: {key.decode()}")

# Espera el primer mensaje del cliente para obtener su dirección
print("Esperando contacto del cliente...")
data, clientAddress = serverSocket.recvfrom(1024)
print(f"  Cliente conectado en {clientAddress[0]}:{clientAddress[1]}")

# Si se pasa el argumento -l, crea el archivo de logueo
logToFile = "-l" in sys.argv
if logToFile:
    filePath = "logs/serverUDPLog_encrypted.txt" if encrypt else "logs/serverUDPLog.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"  Log de ejecución guardado en archivo '{filePath}'")


for i in range(1, totalPackets + 1):
    tx_message = f"{groupName} - {i}"
    tx_bytes = fernet.encrypt(tx_message.encode()) if encrypt else tx_message.encode()

    # El paquete incluye un header de 4 bytes que indica el largo del mensaje para detectar correctamente el limite entre uno y otro
    packet = struct.pack('!I', len(tx_bytes)) + tx_bytes
    serverSocket.sendto(packet, clientAddress)

    logMessage = f"Mensaje {i} enviado - '{tx_message}' - {datetime.now()}\n"
    if logToFile: 
        logFile.write(logMessage)
    else:
        print(logMessage.strip())

    time.sleep(sleepTime)

print(f"  {totalPackets} paquetes enviados con éxito al cliente.\nCerrando ejecución...")
if logToFile:
    logFile.close()
serverSocket.close()