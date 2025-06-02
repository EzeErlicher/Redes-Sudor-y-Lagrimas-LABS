import socket
import struct

HOST = 'localhost'
PORT = 9090

groupName = "Redes, sudor y lágrimas"
packetCount = 0           # Contador de paquetes recibidos
totalPackets = 100          # Cantidad de paquetes a recibir

logToConsole = True
logToFile = False

# Crea el socket TCP y la solicitud de conexión al servidor
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientSocket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("ERROR: Falló la conexión porque el servidor no está disponible.")
    exit()

print("Conexión con el servidor exitosa.")

while packetCount < totalPackets:
    try:
        # Recibe cabecera (4 bytes)
        header = b''
        while len(header) < 4:
            data = clientSocket.recv(4 - len(header))
            if not data:
                print("ERROR: Header del paquete invalido")
                break
            header += data
        msg_length = struct.unpack('!I', header)[0]  # Decodifica longitud
        
        # Recibe el cuerpo del paquete con la cantidad de bytes definidos por el header
        body = b''
        while len(body) < msg_length:
            data = clientSocket.recv(msg_length - len(body))
            if not data:
                print("ERROR: Cuerpo del paquete invalido")
                break
            body += data
        
        if len(body) < msg_length:
            break  # Cuerpo incompleto
        
        rx_message = body.decode('utf-8')
        #print(f"  Server: '{rx_message}'")
        packetCount += 1

    except (ConnectionAbortedError, ConnectionResetError):
        print("ERROR: Se cayó el server.")
        break

print(f"Total de paquetes recibidos: {packetCount}")
clientSocket.close()
