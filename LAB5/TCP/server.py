import socket
from datetime import datetime

HOST = 'localhost'
PORT = 9090

# Cierre del socket de conexión con el cliente
def closeSocket(connectionSocket,clientCount):
    connectionSocket.send("Desconexión exitosa".encode())
    connectionSocket.close()
    print(f" Cliente {clientCount} se ha desconectado exitosamente.")

# Crea el socket TCP por IPv4 y lo asocia a la dirección especificada
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))

# Escucha solicitudes de conexión con maximo 1 conexión esperando en cola
serverSocket.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}")

clientCount = 0           # Contador de conexiones recibidas
waitingForClient = True   # Variable auxiliar para aceptar nuevas conexiones

while True:

    # Espera nuevo cliente
    if waitingForClient:
        # Acepta al cliente creando su socket especifico
        connectionSocket, addr = serverSocket.accept()

        clientCount += 1
        waitingForClient = False
        print(f"\n Cliente {clientCount} conectado en {addr[0]}:{addr[1]}")

        # Envía un mensaje de confirmación de conexión exitosa
        tx_message = f"Bienvenido cliente {clientCount}! Felicitaciones por una conexión exitosa con el servidor. La hora es {datetime.now().strftime("%H:%M")}"
        connectionSocket.send(tx_message.encode())

    # Espera a un mensaje del cliente, en caso de falla cierra el socket de conexión
    try:
        rx_message = connectionSocket.recv(1024).decode()
    except (ConnectionResetError, ConnectionAbortedError):
        print(f" Cliente {clientCount} se desconectó inesperadamente.")
        connectionSocket.close()
        waitingForClient = True
        continue

    if "close" in rx_message.lower():               # Comando para cerrar la conexión
        closeSocket(connectionSocket,clientCount)
        waitingForClient = True
    elif "shutdown" in rx_message.lower():          # Comando para cerrar el servidor
        closeSocket(connectionSocket,clientCount)
        print("\nApagando servidor...")
        break
    else :                                          # Mensaje del cliente
        print(f"	Mensaje recibido de cliente {clientCount}: '{rx_message}'")
        connectionSocket.send(f'Mensaje "{rx_message}" recibido!'.encode())