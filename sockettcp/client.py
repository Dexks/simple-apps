from socket import *

# ########## CHANGE HERE ########### #

# IP and PORT for TCP connection
IP = "127.0.0.1"
PORT = 43210

# ########## CHANGE HERE ########### #


# Receive data, decode it and clears "\n"
def recv(client):
    data = client.recv(1024).decode().strip()
    return data


# Sends data in bytes
def send(data, client):
    client.send(data.encode())


# Connects to IP and address
def connect():
    datatosend = "Hello, server"

    # Creates SOCKET TCP object
    client = socket(AF_INET, SOCK_STREAM)

    # Connects to the address (IP and PORT)
    client.connect((IP, PORT))

    # Sends "datatosend" data
    send(datatosend, client)
    print("Data sent:", datatosend)

    # Receives and prints data
    data = recv(client)
    print("Data received:", data)
    client.close()


if __name__ == "__main__":
    connect()
