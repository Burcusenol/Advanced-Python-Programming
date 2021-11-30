from pytube import YouTube
from tkinter import filedialog, font
from tkinter import ttk
from tkinter import *
import re
import threading



class Application:
    def __init__(self,root):
        self.root=root
        self.root.grid_rowconfigure(0,weight=2)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.config(bg="#ffdddd")        
        self.top_label=Label(self.root,text="YOUTUBE DOWNLOAD MANAGER",fg="orange",font=("Type Xero",70))
        self.top_label.grid(pady=(1,10))
        self.linkLabel=Label(self.root,text="Paste the YouTube Link Below",font=('Snowpersons',30))
        self.linkLabel.grid(pady=(0,20))
        self.youtubeEntryVar = StringVar()
        self.youtubeEntry=Entry(self.root,width=70,textvariable=self.youtubeEntryVar,font=("Agency Fb",25),fg="green")
        self.youtubeEntry.grid(pady=(0,15),ipady=2)
        self.youtubeEntryError=Label(self.root,text="",font=("Concert One",20))
        self.youtubeEntryError.grid(pady=(0,8))
        self.youtubeFileSaveLabel=Label(self.root,text="Choose Directory",font=("Variety",30))
        self.youtubeFileSaveLabel.grid()
        self.youtubeFileDirectoryButton=Button(self.root,text="Directory",font=("Bell MT",15),command=self.openDirectory)
        self.youtubeFileDirectoryButton.grid(pady=(10,3))
        self.fileLocationLabel=Label(self.root,text="",font=("Agency Fb",20))
        self.fileLocationLabel.grid()
        self.youtubeChooseLabel=Label(self.root,text="Choose the Download Type",font=("Variety",30))
        self.youtubeChooseLabel.grid()
        
        downloadChoices=[("Audio MP3",1),("Video MP4",2)]
        self.ChoicesVar=StringVar()
        self.ChoicesVar.set(1)
        
        for text,mode in downloadChoices:
            self.youtubeChoices=Radiobutton(self.root,text=text,font=("Northwest old",15),variable=self.ChoicesVar,value=mode)
            self.youtubeChoices.grid()
            
        self.youtubedownloadButton=Button(self.root,text="Download",width=10,command=self.checkyoutubeLink,font=("Bell MT",15))
        self.youtubedownloadButton.grid(pady=(30,50))
        
        
    def checkyoutubeLink(self):
        self.matchyoutubeLink=re.match("^https://www.youtube.com/.",self.youtubeEntryVar.get())
        
        if(not self.matchyoutubeLink):
            self.youtubeEntryError.config(text="Invalid Youtube Link",fg="red")
        elif(not self.openDirectory()):
            self.youtubeFileSaveLabel.config(text="Please Choose the Folder",fg="red")
        elif(self.matchyoutubeLink and self.openDirectory()):
            self.downloadWindow()
        
        
    def downloadWindow(self):
        self.newWindow=Toplevel(self.root)
        self.root.withdraw()
        self.app=SecondPage(self.newWindow,self.youtubeEntryVar.get(),self.FolderName.get(),self.ChoicesVar.get())        
        
        
        
        
        
    def openDirectory(self):
        self.FolderName=filedialog.askdirectory()
        if(len(self.FolderName)>0):
            self.fileLocationLabel.config(text=self.FolderName,fg="green",font=("Freestyle script",25))
            return True
        else:
            self.fileLocationLabel.config(text="Please Choose the Folder",fg="red",font=("Freestyle script",25))
        



if __name__=="__main__":
    window = Tk()
    window.state("zoomed")
    app=Application(window)
    window.mainloop()