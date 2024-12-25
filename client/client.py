import socket
import threading
import time
import pyperclip

from server.config import HOST, PORT

# Function to monitor clipboard content
def monitor_clipboard(client_socket):
    previous_clipboard_content = ""
    
    while True:
        try:
            # Get the current clipboard content
            current_clipboard_content = pyperclip.paste()
            
            # If the clipboard content has changed
            if current_clipboard_content != previous_clipboard_content:
                print(f"Clipboard changed: {current_clipboard_content}")
                
                # Send the new clipboard content to the server
                client_socket.sendto(current_clipboard_content.encode(), (HOST, PORT))
                
                # Update the previous clipboard content
                previous_clipboard_content = current_clipboard_content
            
            # Check clipboard every second
            time.sleep(1)
        except socket.error as e:
            print(f"Socket error: {e}")
            break  # Exit the loop if there's a socket error
        except Exception as e:
            print(f"Error monitoring clipboard: {e}")
            time.sleep(1)  # Sleep for a second to avoid tight error loop

# Function to start the client, listen for server messages, and handle clipboard
def start_client():
    # Start listening for messages in a from UDP server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)  # timeout for receiving messages
    
    # Start a thread to monitor clipboard content
    threading.Thread(target=monitor_clipboard, args=(client_socket,), daemon=True).start()

    try:
        while True:
            try:
                # Listen for incoming messages (such as clipboard updates)
                data, addr = client_socket.recvfrom(1024)
                print(f"Received message from {addr}: {data.decode('utf-8')}")
            except socket.timeout:
                pass  # Continue looping if no message is received
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    except KeyboardInterrupt:
        print("Shutting down client...")
    finally:
        client_socket.close()
        print("Socket closed")

if __name__ == "__main__":
    start_client()

