from tkinter import *
from PIL import ImageTk,  ImageTk
import requests


root=Tk()
root.config(bg='#FDFFFC')
root.title('weather app')
root.geometry("700x350")
frame=LabelFrame(root,bg='#FDFFFC',fg='#FDFFFC')
frame.pack(fill='both',expand='yes',side=BOTTOM)

city_name=StringVar()

   
   
def search(event):
    city=city_name.get()
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=ddd374a4ce1fe9f9bcf9c53b2a78732e&units=metric".format(city)
    res=requests.get((url))
    data=res.json()
    temp=data['main']['temp']
    #set_image(temp)
    
    data_lbl=Label(frame,text=temp,font=('cenutry gothic',16),bg='#FDFFFC')
    data_lbl.pack()
    city_name.set('')
    
label=Label(root,text='City Name',font=('cenutry gothic',16),bg='#FDFFFC').pack()
city_box=Entry(root,textvariable =city_name,font=('cenutry gothic',16))
city_box.bind('<Return>',search)

city_box.pack()





root.mainloop()