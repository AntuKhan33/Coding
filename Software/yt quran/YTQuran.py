from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube



Folder_Name=''




def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if (len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg='green')
    else:
        locationError.config(text='please chose folder',fg='red')
        
        
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text='')
        yt=YouTube(url)   
        if (choice==choices[0]):
            select=yt.streams.filter(progressive=True).first()
        elif (choice==choices[1]):
            select=yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice==choices[2]):    
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(Text='paste link again',fg='red')
            
            
            
        select.download(Folder_Name)
        ytdError.config(text="download complete")    
root=Tk()
root.title(" YT Quran Downloader")
root.geometry('350x400')
root.columnconfigure(0,weight=1)





#ytd link lebel
ydtLabel=Label(root,text="Enter the URL of video",font=('Jost',15))
ydtLabel.grid()



ytdEntryvar=StringVar()
ytdEntry=Entry (root,width=50,textvariable=ytdEntryvar)
ytdEntry.grid()



ytdError=Label (root,text='Error msg',fg='red')
ytdError.grid()


saveLabel=Label(root,text='save the video file',font=('jost',15,'bold'))
saveLabel.grid()

saveEntry=Button(root,width=10,bg='red',text="chose path",command=openLocation)
saveEntry.grid()


locationError=Label(root,text='Error msg of path',fg='red',font=('jost,15'))
locationError.grid()

ytdQuality=Label(root,text='select quality')
ytdQuality.grid()

choices=['720p','144p','only audio']
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn=Button(root,text='Download',width=10,bg='red',fg='white',command=DownloadVideo)
downloadbtn.grid()


developerlabel=Label(root,text="Dream developer",font=('jost',15))
developerlabel.grid()



root.mainloop()