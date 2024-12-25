import sys
from server.server import start_server
from client.client import start_client

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        start_server()
    else:
        start_client()

