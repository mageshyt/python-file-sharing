def broadcast_event(content, clients):
    print(f"Broadcasting event: {content}")
    for client in clients:
        try:
            client.sendto(content.encode("utf-8"), client.getpeername())
        except Exception as e:
            print(f"Error broadcasting to {client}: {e}")
