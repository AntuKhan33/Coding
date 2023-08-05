from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk
import threading
import os
import tkinter as tk
threads = {}
def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)    
        
def Open():
    window = tk.Tk()
    window.title("JOHN CENA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    window.geometry("620x400")
    window.configure(background='grey')
    img = ImageTk.PhotoImage(Image.open(resource_path("JC_image.jpg")), master=window)
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.attributes("-topmost", True)
    window.mainloop()

def on_press(key):
    try:
        KEY = key.char.lower()
        if KEY in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            thread_id = len(threads) + 1
            threads[thread_id] = threading.Thread(target=Open)
            threads[thread_id].start()
    except:
        pass
    return True

with Listener(on_press=on_press) as listener:
    listener.join()
