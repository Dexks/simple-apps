from socket import *

# ########## CHANGE HERE ########### #

# IP and PORT for TCP listener
SERVER_IP = "127.0.0.1"
SERVER_PORT = 43210

# if True, the server will keep listening for new connections after ending one
PERSISTENT = False

# ########## CHANGE HERE ########### #


# Receive data, decode it and clears "\n"
def recv(connected):
    data = connected.recv(1024).decode().strip()
    return data


# Sends data in bytes
def send(connected, data):
    connected.send(data.encode())


# Listens to connections
def listen():
    # Creates SOCKET TCP object
    server = socket(AF_INET, SOCK_STREAM)

    # Binds the socket "server" to the SERVER_IP and PORT
    server.bind((SERVER_IP, SERVER_PORT))

    # Listen to connections
    server.listen(1)

    datatosend = "Hello, client"

    while True:
        print("Waiting connection...")
        # Await a connection
        connected, client = server.accept()

        # Prints the client tuple (ip, port)
        print("Connection from -> ", client)

        # Awaits and prints the received message
        data = recv(connected)
        print("Data received:", data)

        # Sends "datatosend" data
        send(connected, datatosend)
        print("Data sent:", datatosend)

        # Closes the connection
        connected.close()

        if not PERSISTENT:
            break


if __name__ == "__main__":
    listen()
