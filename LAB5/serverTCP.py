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
sleepTime = 0.5        # Espera en segundos entre el envío de un paquete y el siguiente

# Crea el socket TCP por IPv4 y lo asocia a la dirección especificada
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)  # Escucha solicitudes de conexión con maximo 1 conexión esperando en cola

print(f"Servidor escuchando en {HOST}:{PORT}")

connectionSocket, addr = serverSocket.accept()
print(f"  Cliente conectado en {addr[0]}:{addr[1]}")

# Revisar si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    # Archivo de logueo de los envios de paquetes
    filePath = f"logs/serverTCPLog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"  Log de ejecución guardado en archivo '{filePath}'")

for i in range(1, totalPackets + 1):
    tx_message = f"{groupName} - {i}"
    # Paquete = Cabecera + Contenido
    packet = struct.pack('!I', len(tx_message.encode())) + tx_message.encode()

    connectionSocket.sendall(packet)
    logMessage = f"Mensaje {i} enviado - '{tx_message}' - {datetime.now()}\n"

    logFile.write(logMessage) if logToFile else print(logMessage.strip())

    time.sleep(sleepTime)

print(f"  {totalPackets} paquetes enviados con exito al cliente.\nCerrrando ejecución...")
connectionSocket.close()
