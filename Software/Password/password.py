from tkinter import *
import string
import random

def generate_password():
    password=[]
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        passwords = " ".join(str(x)for x in password)
        label.config(text=passwords)

    
root = Tk()
root.geometry("400x300")
button = Button(root, text="Generate Password", command=generate_password)
button.grid(row=1, column=1)
label = Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=2)
root.mainloop()
