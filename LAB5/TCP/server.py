import socket
import struct
from datetime import datetime

# IP local de la computadora
HOST = 'localhost'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
totalPackets = 100    # Cantidad de paquetes a transmitir

# Crea el socket TCP por IPv4 y lo asocia a la dirección especificada
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
# Escucha solicitudes de conexión con maximo 1 conexión esperando en cola
serverSocket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}")

connectionSocket, addr = serverSocket.accept()
print(f"  Cliente conectado en {addr[0]}:{addr[1]}")

for i in range(totalPackets):
    tx_message = f"{groupName} - {i+1}"

    body = tx_message.encode()
    header = struct.pack('!I', len(body))
    packet = header + body

    connectionSocket.sendall(packet)  # Envia cabecera + cuerpo

print(f"  {totalPackets} paquetes enviados con exito al cliente.\nCerrrando ejecución...")
connectionSocket.close()