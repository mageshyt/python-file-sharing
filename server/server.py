import threading

from common.network import bind_socket, create_udp_socket  # Corrected the function name
from server.config import HOST, PORT


clients = []  # List of client addresses (IP, PORT)

def handle_client(server, client_address):
    while True:
        try:
            # Receive message from client
            message, addr = server.recvfrom(1024)
            if message:
                print(f"Received '{message.decode('utf-8')}' from {client_address}")

                # Broadcast message to all clients
                for client in clients:
                    if client != client_address:  # Don't send the message back to the sender
                        server.sendto(message, client)
            else:
                break  # If message is empty, close the connection
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    print(f"Connection from {client_address} closed")

def start_server():
    try:
        server = create_udp_socket()  # Use UDP socket
        bind_socket(server, HOST, PORT)  # Bind to the host and port
        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            message, client_address = server.recvfrom(1024)  # Receive message from any client
            if client_address not in clients:  # Only add the client once
                clients.append(client_address)  # Add the client address to the clients list
                print(f"New client connected: {client_address}")
            
            # Start a new thread to handle the client
            threading.Thread(target=handle_client, args=(server, client_address)).start()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_server()

