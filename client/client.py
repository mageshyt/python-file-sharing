import socket
import threading
from common.network import create_udp_socket
from common.clipboar import update_clipboard
from client.config import SERVER_IP, SERVER_PORT

def receive_message(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(f"Received: {message}")
            update_clipboard(message)

def send_message(client_socket):
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

def start_client():
    client_socket = create_udp_socket()
    print(f"Connecting to server {SERVER_IP}:{SERVER_PORT}")
    client_socket.connect((SERVER_IP, SERVER_PORT))

    threading.Thread(target=receive_message, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()

if __name__ == "__main__":
    start_client()
