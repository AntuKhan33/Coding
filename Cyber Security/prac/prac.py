
from pynput import mouse
from pynput import keyboard
from  pynput .mouse import Controller
from  pynput .keyboard import Controller

def controlmouse():
    mouse=Controller()
    mouse.position=(10,20)

def controkeyboard():
    keyboard=Controller()
    keyboard.type("hi how are you")
controkeyboard()

with open ('hello.txt',"w") as f:
    f.write("hi how are you")
