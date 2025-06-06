import socket
import struct
from datetime import datetime
import sys
from cryptography.fernet import Fernet

# IP del servidor en la red local
HOST = '192.168.0.165'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
packetCount = 0           # Paquetes recibidos
totalPackets = 100        # Paquetes a recibir

# Crea el socket TCP y la solicitud de conexión al servidor
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientSocket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("ERROR: Falló la conexión porque el servidor no está disponible.")
    sys.exit()

print("Conexión con el servidor exitosa.")

encrypt = "-e" in sys.argv
if encrypt:
    try:
        key_index = sys.argv.index("-e") + 1
        key = sys.argv[key_index].encode()
        fernet = Fernet(key)
        print(f" Desencriptación activada con clave: '{key.decode()}'")
    except (IndexError, ValueError):
        print(" ERROR: No se proporcionó una clave luego del argumento -e.")
        sys.exit(1)
    except Exception as e:
        print(f" ERROR: Clave Fernet inválida - {e}")
        sys.exit(1)

# Activar logueo si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    filePath = "logs/clientTCPLog_encrypted.txt" if encrypt else "logs/clientTCPLog.txt"
    logFile = open(filePath, "w", encoding="utf-8")
    print(f" Log de ejecución guardado en archivo '{filePath}'")

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
        print(f"ERROR: Falló la recepción del paquete {packetCount+1}")
        break

    if encrypt: body = fernet.decrypt(body)
    rx_message = body.decode('utf-8')
    
    logMessage = f"Mensaje {packetCount+1} recibido - '{rx_message}' - {datetime.now()}\n"
    logFile.write(logMessage) if logToFile else print(logMessage.strip())

    packetCount += 1

print(f"Total de paquetes recibidos: {packetCount}")
clientSocket.close()
if logToFile: logFile.close()