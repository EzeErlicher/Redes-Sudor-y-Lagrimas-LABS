import socket
import struct
from datetime import datetime
import sys

# IP local del servidor
HOST = 'localhost'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
packetCount = 0
totalPackets = 10

# Crea el socket UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente UDP iniciado.")

# Envía un mensaje inicial para notificar al servidor de su dirección
clientSocket.sendto(b"Hola servidor!", (HOST, PORT))

# Revisar si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    filePath = f"logs/clientUDPLog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"Log de ejecución guardado en archivo '{filePath}'")

while packetCount < totalPackets:
    try:
        packet, addr = clientSocket.recvfrom(4096)
        if not packet:
            break

        # Procesa cabecera (4 bytes)
        if len(packet) < 4:
            print(f"ERROR: Paquete {packetCount+1} demasiado corto.")
            break
        msg_length = struct.unpack('!I', packet[:4])[0]
        body = packet[4:]
        if len(body) != msg_length:
            print(f"ERROR: Paquete {packetCount+1} tamaño inconsistente.")
            break

        rx_message = body.decode('utf-8')
        logMessage = f"Mensaje {packetCount+1} recibido - '{rx_message}' - {datetime.now()}\n"
        logFile.write(logMessage) if logToFile else print(logMessage.strip())
        packetCount += 1

    except socket.timeout:
        print("ERROR: Timeout de recepción.")
        break

print(f"Total de paquetes recibidos: {packetCount}")
clientSocket.close()
if logToFile: logFile.close()
