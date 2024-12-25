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
