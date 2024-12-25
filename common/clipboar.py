import pyperclip

def update_clipboard(text):
    """
    update the system clipboard with given text
    """
    pyperclip.copy(text)

    print("Cliboard updated" )

def get_clipboard():
    """
    get the text from the system clipboard
    """
    return pyperclip.paste()


if __name__ == "__main__":
    update_clipboard("Hi bro how are you!")
    print(get_clipboard())

