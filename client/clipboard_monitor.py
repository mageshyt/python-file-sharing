import time
import pyperclip  # Library to monitor clipboard content
import socket

from common.network import create_udp_socket
from server.config import HOST, PORT

def monitor_clipboard():
    previous_clipboard_content = ""
    server_socket = create_udp_socket()
    
    while True:
        try:
            # Get the current clipboard content
            current_clipboard_content = pyperclip.paste()
            
            # If the clipboard content has changed
            if current_clipboard_content != previous_clipboard_content:
                print(f"Clipboard changed: {current_clipboard_content}")
                
                # Send the new clipboard content to the server
                server_socket.sendto(current_clipboard_content.encode('utf-8'), (HOST, PORT))
                
                # Update the previous clipboard content
                previous_clipboard_content = current_clipboard_content
            
            # Check clipboard every second
            time.sleep(1)
        except Exception as e:
            print(f"Error monitoring clipboard: {e}")
            break

