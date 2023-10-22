
import socket
import select
import sys

# initiate Client socket with the TCP connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the client socket with the localhost as ip and port number
port = 5606

# try to connect to the server with associated port and id
client_socket.connect(('192.168.1.14', port)) # '127.0.0.1' is the localhost in ipv4

# open a connection until sending CLOSE SOCKET
while True:
    message = input("enter your message: ") # send message as bytes
    client_socket.send(message.encode()) # send message as bytes

    # recieve response if exists
    readable, _, _ = select.select([client_socket], [], [], 10)

    if readable:
        response = client_socket.recv(1024).decode()
        print("Received response: " + response)

    if message == 'CLOSE SOCKET':
        print('Closing connection')
        client_socket.close()
        break