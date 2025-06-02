import socket
import struct
import time
from datetime import datetime
import sys

# IP local de la computadora
HOST = 'localhost'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
totalPackets = 10    # Cantidad de paquetes a transmitir
sleepTime = 0.5      # Espera en segundos entre el envío de un paquete y el siguiente

# Crea el socket UDP por IPv4
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((HOST, PORT))
print(f"Servidor UDP escuchando en {HOST}:{PORT}")

# Espera el primer mensaje del cliente para obtener su dirección
print("Esperando contacto del cliente...")
data, clientAddress = serverSocket.recvfrom(1024)
print(f"  Cliente conectado en {clientAddress[0]}:{clientAddress[1]}")

# Revisar si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    # Archivo de logueo de los envios de paquetes
    filePath = f"logs/serverUDPLog.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"  Log de ejecución guardado en archivo '{filePath}'")

for i in range(1, totalPackets + 1):
    tx_message = f"{groupName} - {i}"
    # Paquete = Cabecera + Contenido
    packet = struct.pack('!I', len(tx_message.encode())) + tx_message.encode()
    serverSocket.sendto(packet, clientAddress)
    
    logMessage = f"Mensaje {i} enviado - '{tx_message}' - {datetime.now()}\n"
    logFile.write(logMessage) if logToFile else print(logMessage.strip())
    
    time.sleep(sleepTime)

print(f"  {totalPackets} paquetes enviados con éxito al cliente.\nCerrando ejecución...")
if logToFile: logFile.close()
serverSocket.close()