import time
from pynput.keyboard import  Controller, Key,Listener
keyboard=Controller()



keyboard.type('This is one line.\nAnd this is the next line.\n\tThis line has been tabbed in.')
