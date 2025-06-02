import socket
import struct
from datetime import datetime
import sys

# IP local del servidor
HOST = 'localhost'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
packetCount = 0           # Contador de paquetes recibidos
totalPackets = 100          # Cantidad de paquetes a recibir

# Crea el socket TCP y la solicitud de conexión al servidor
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientSocket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("ERROR: Falló la conexión porque el servidor no está disponible.")
    exit()

print("Conexión con el servidor exitosa.")

# Revisar si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    filePath = f"logs/clientTCPLog.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f"Log de ejecución guardado en archivo '{filePath}'")

# Recibe exactamente 'num_bytes' bytes del socket.
def recv_exact(sock, num_bytes):
    buffer = b''
    while len(buffer) < num_bytes:
        try:
            chunk = sock.recv(num_bytes - len(buffer))
            if not chunk:
                return None  # Desconexión o paquete incompleto
            buffer += chunk
        except (ConnectionAbortedError, ConnectionResetError):
            return None      # Error de conexión
    return buffer

while packetCount < totalPackets:
    # Recibe cabecera (4 bytes)
    header = recv_exact(clientSocket, 4)
    if header is None:
        print(f"ERROR: Falló la recepción del header del paquete {packetCount+1}")
        break
    msg_length = struct.unpack('!I', header)[0]  # Decodifica longitud
    
    # Recibe el cuerpo del paquete con la cantidad de bytes definidos por el header
    body = recv_exact(clientSocket, msg_length)
    if body is None:
        print(f"ERROR: Falló la recepción del cuerpo del paquete {packetCount+1}")
        break

    rx_message = body.decode('utf-8')
    logMessage = f"Mensaje {packetCount+1} recibido - '{rx_message}' - {datetime.now()}\n"
    logFile.write(logMessage) if logToFile else print(logMessage.strip())

    packetCount += 1

print(f"Total de paquetes recibidos: {packetCount}")
clientSocket.close()
if logToFile: logFile.close()