import pyperclip
import time

last_clipboard_content = ""  # To store the last clipboard content

def broadcast_clipboard_content(server,clients):
    global last_clipboard_content
    while True:
        try:
            # Check the clipboard for new content
            clipboard_content = pyperclip.paste()

            # If the clipboard content has changed, broadcast it to all clients
            if clipboard_content != last_clipboard_content:
                print(f"Clipboard updated: {clipboard_content}")
                last_clipboard_content = clipboard_content

                # Broadcast the new clipboard content to all connected clients
                for client in clients:
                    server.sendto(clipboard_content.encode('utf-8'), client)

            # Poll every 1 second to check for new clipboard content
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred while checking clipboard: {e}")

