import socket


def create_udp_socket():
    """
        Create a UDP socket  and return it
    """
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def bind_socket(socket, address, port):
    """
        Bind the socket to the address and port
    """
    socket.bind((address, port))


def send_message(message,host,port):
    """
        Send a message to the specified host and port
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode("utf-8"), (host, port))

def listen_for_messages():
    """
        Listen for incoming messages
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 5000))  # Listening on all interfaces, port 5000

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode('utf-8')}")
