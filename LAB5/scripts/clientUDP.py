import socket
import struct
from datetime import datetime
import sys
from cryptography.fernet import Fernet

# IP del servidor en la red local
HOST = '192.168.0.12'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
packetCount = 0           # Paquetes recibidos
totalPackets = 100        # Paquetes a recibir

# Crea el socket UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente UDP iniciado.")

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

# Envía un mensaje inicial para notificar al servidor de su dirección
clientSocket.sendto(b"Hola servidor!", (HOST, PORT))

# Revisar si se pasa el argumento -l
logToFile = "-l" in sys.argv
if logToFile:
    filePath = "logs/clientUDPLog_encrypted.txt" if encrypt else "logs/clientUDPLog.txt" 
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

        try:
            rx_message = body.decode('utf-8') if not encrypt else fernet.decrypt(body).decode('utf-8')
        except Exception as e:
            print(f" ERROR: Fallo al desencriptar el paquete {packetCount+1}")
            break
 
        logMessage = f"Mensaje {packetCount+1} recibido - '{rx_message}' - {datetime.now()}\n"
        logFile.write(logMessage) if logToFile else print(logMessage.strip())
        packetCount += 1

    except (ConnectionResetError, ConnectionRefusedError):
        print(" ERROR: Servidor caido / no disponible")
        break

print(f"Total de paquetes recibidos: {packetCount}")
if logToFile: logFile.close()
clientSocket.close()