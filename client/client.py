import threading
from common.network import  listen_for_messages
from client.clipboard_monitor import monitor_clipboard


# Function to listen for messages (like clipboard updates from server or other clients)
def start_client():
    # Start listening for incoming messages (this can be clipboard updates or other events)
    threading.Thread(target=listen_for_messages, daemon=True).start()

    # Start monitoring clipboard for changes
    monitor_clipboard()


if __name__ == "__main__":
    start_client()

