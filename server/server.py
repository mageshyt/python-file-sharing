import socket
import threading
from server.event_broadcast import broadcast_event
from common.network import create_udp_socket, bind_socket
from server.config import HOST, PORT

clients = []  # List to keep track of connected clients

# Function to manage client connections and handle incoming messages
def handle_client(client_socket, client_address):
    clients.append(client_socket)  # Add client to the list when they connect

    try:
        while True:
            data, addr = client_socket.recvfrom(1024)
            message = data.decode("utf-8")
            print(f"Received clipboard content from {addr}: {message}")
            # Broadcast the message (clipboard content) to all other clients
            broadcast_event(message, clients)  # Pass the clients list to the broadcast function
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        # Remove client from the list when disconnected
        clients.remove(client_socket)
        print(f"Connection closed: {client_address}")

def start_server():
    try:
        server_socket = create_udp_socket()
        bind_socket(server_socket, HOST, PORT)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            data, client_address = server_socket.recvfrom(1024)  # Receive initial connection request
            print(f"New connection from {client_address}")
            threading.Thread(target=handle_client, args=(server_socket, client_address)).start()
    except Exception as e:
        print(f"An error occurred: {e}")
