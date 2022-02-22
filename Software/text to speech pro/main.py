from tkinter import * 
from tkinter import ttk
import random
root=Tk()
root.geometry('1280x720')
root.title("Text To Speech")

def blind():
    color=['yellow','red','blue','green']
    a=random.choice(color)
    lbl_title.configure(bg=a)
    lbl_title.after(1000,blind)
    
    
#---------------------------title------------------------------------
lbl_title=Label(root,text="Text To Speech",font='arial 50 bold')
lbl_title.place(x=0,y=0,relwidth=1)

f1=Frame(root,relief=GROOVE,bd=5)
f1.place(x=10,y=100,width=605,height=300)
txt_area=Text(f1,font=('times new rommon',15,'bold'),bg='grey99')
txt_area.place(x=10,y=5)

gender_lvl=Label(root,text="Gender",font=('Impack 25 bold'),width=8,bg='yellow',fg='red')
gender_lvl.place(x=30,y=410)

speed_lvl=Label(root,text="Speed",font=('Impack 25 bold'),width=9,bg='yellow',fg='red')
speed_lvl.place(x=230,y=410)

volume_lvl=Label(root,text="Volume",font=('Impack 25 bold'),width=8,bg='yellow',fg='red')
volume_lvl.place(x=450,y=410)



gender_combo=ttk.Combobox(root,values=['Male','Female'],width=16,font='arial 12 bold',state='r')
gender_combo.place(x=30,y=500)

speed_combo=ttk.Combobox(root,values=['Fast','Normal','Slow'],width=18,font='arial 12 bold',state='r')
speed_combo.place(x=230,y=500)

scale_level=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=160)
scale_level.place(x=450,y=480)
scale_level.set(50)


#---------------------------Button------------------------------------
play_btn=Button(root,text='Play',font='arial 25 bold',bg='lime',activebackground='yellow',relief=SUNKEN,bd=10)
play_btn.place(x=60,y=550)
d_btn=Button(root,text='Download',width=8,font='arial 25 bold',bg='lime',activebackground='yellow',relief=SUNKEN,bd=10)
d_btn.place(x=230,y=550)

root.configure(bg='powderblue')
blind()

root.mainloop()