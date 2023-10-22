import socket
import threading

PORT = 5606
ADDR = ('192.168.1.14', PORT)

# Data structure to store client information
client_list = []

# Functionality of the server
def handle_client(conn, addr):
    print("[NEW CONNECTION] " + str(addr) + " connected.")

    # Store client information
    client_info = {
        "socket": conn,
        "address": addr
    }
    client_list.append(client_info)

    while True:
        data = conn.recv(1024).decode()
        if data == "CLOSE SOCKET":
            break
        else:
            response = data.upper()
            conn.send(response.encode())
    
    # Remove client from list after disconnection
    client_list.remove(client_info)
    conn.close()
    print("[CONNECTION CLOSED] " + str(addr))

# Main server function
def main():
    print("Server is starting...")

    # Open server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    while True:
        conn, addr = server.accept()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        # Start a new thread to handle the client connection
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()

