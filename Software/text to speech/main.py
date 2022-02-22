from tkinter import *
import pyttsx3
root=Tk()
root.title('Text to Speech')
root.geometry("800x500")

def talk():
    engine=pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0,END)

entry=Entry(root,font=("Helvetica",18))
entry.pack()

btn=Button(root,text="speak",command= talk)
btn.pack()
root.mainloop()