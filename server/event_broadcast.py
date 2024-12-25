def broadcast_event(content, clients, server_socket):
    for client_address in clients:
        try:
            # Send message to each client using their address
            server_socket.sendto(content.encode("utf-8"), client_address)
        except Exception as e:
            print(f"Error broadcasting to {client_address}: {e}")

