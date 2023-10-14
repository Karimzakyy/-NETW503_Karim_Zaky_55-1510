
import socket
import select
import sys

# initiate server socket with the TCP connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the server socket with the localhost as ip and port number
port = 5615
server_socket.bind(('192.168.1.14', port)) # '127.0.0.1' is the localhost in ipv4

# make the socket listen on this port
server_socket.listen(5)

# listening forever
while True:
    # accept connection from a client
    client, addr = server_socket.accept()
    print('Connection established with ' + str(addr))

    # open a conditional connection --> break the connection when 'CLOSE SOCKET' is received
    while True:
        # check if there is any data to be read from the client
        readable, _, _ = select.select([client], [], [], 10)

        if readable:
            # recieve message as bytes
            message = client.recv(1024).decode()

            # check if the message was 'CLOSE SOCKET' to close connection
            if message == 'CLOSE SOCKET':
                print('Connection closed by client')
                client.close()
                break

            # otherwise capitalize the decoded message
            response = message.upper()

            # send the response as bytes again
            client.send(response.encode())

