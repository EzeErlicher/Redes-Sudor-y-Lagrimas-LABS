import socket

HOST = 'localhost'
PORT = 9090

# Crea el socket TCP y la solicitud de conexión al servidor
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientSocket.connect((HOST, PORT))
except ConnectionRefusedError:
    print("ERROR: Falló la conexión porque el servidor no está disponible.")
    exit()

# Recibe el mensaje inicial del servidor
rx_message = clientSocket.recv(1024)
print(f"\nServer: '{rx_message.decode()}'")

while True:
    # Envía el input del usuario al servidor
    tx_message = input("   Escriba su mensaje: ")
    clientSocket.send(tx_message.encode())

    # Espera la respuesta del servidor, en caso de falla cierra el socket
    try:
        rx_message = clientSocket.recv(1024)
        print(f"Server: '{rx_message.decode()}'")
    except (ConnectionAbortedError, ConnectionResetError):
        print("ERROR: Se cayó el server.")
        break

    # Si se envió un comando de cierre o apagado, cierra el socket
    if "close" in tx_message or "shutdown" in tx_message:
        break

print("")
clientSocket.close()