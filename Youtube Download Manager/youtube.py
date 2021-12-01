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
        elif(not self.openDirectory):
            self.fileLocationLabel.config(text="Please Choose the Folder",fg="red")
        elif(self.matchyoutubeLink and self.openDirectory):
            self.downloadWindow()
           
            
        
    def downloadWindow(self):
        self.newWindow=Toplevel(self.root)
        self.root.withdraw()
        self.app=SecondPage(self.newWindow,self.youtubeEntryVar.get(),self.FolderName,self.ChoicesVar.get())        
       
    
    def openDirectory(self):
        self.FolderName=filedialog.askdirectory()
        if(len(self.FolderName)>1):
            self.fileLocationLabel.config(text=self.FolderName,fg="green",font=("Freestyle script",25))
            return True
        else:
            self.fileLocationLabel.config(text="Please Choose the Folder",fg="red",font=("Freestyle script",25))
        
     
   
    
class SecondPage:
    def __init__(self,downloadwindow,youtubeEntry,FolderName,Choices):
        self.downloadwindow=downloadwindow
        self.downloadwindow.state("zoomed")
        self.downloadwindow.grid_rowconfigure(0,weight=0)
        self.downloadwindow.grid_columnconfigure(0,weight=1)
        self.youtubeEntry=youtubeEntry
        self.FolderName=FolderName
        self.Choices=Choices
        
        self.yt=YouTube(self.youtubeEntry)
        
        if(self.Choices=="1"):
            self.video_type=self.yt.streams.filter(only_audio=True).first()
            self.maxFileSize=self.video_type.filesize
            
        if(self.Choices=="2"):
            self.video_type=self.yt.streams.first()
            self.maxFileSize=self.video_type.filesize
            
        self.loadingLabel=Label(self.downloadwindow,text="Downloading in Progress...",font=("Small Fonts",40))
        
        self.loadingLabel.grid(pady=(100,0))
        
        self.loadingPercent=Label(self.downloadwindow,text="0",fg="green",font=("Viner Hand ITC",40))
        self.loadingPercent.grid(pady=(50,0))
        
        self.progressbar=ttk.Progressbar(self.downloadwindow,length=500,orient='horizontal',mode="indeterminate")
        self.progressbar.grid(pady=(50,0))
        self.progressbar.start()
        
        threading.Thread(target=self.yt.register_on_complete_callback(self.show_progress_bar)).start()
        
        threading.Thread(target=self.downloadFile).start()
        
    def downloadFile(self):
        if(self.Choices=="1"):
            self.yt.streams.filter(only_audio=True).first().download(self.FolderName)
        elif(self.Choices=="2"):
            self.yt.streams.first().download(self.FolderName)
                
                
    def show_progress_bar(self,streams=None,chunk=None,filehandle=None,bytes_remaining=None):
        
        self.percentCount=float("%0.2"%(100-(100*(bytes_remaining /self.maxFileSize))))    
        
        if(self.percentCount<100):
           self.loadingPercent.config(text=str(self.percentCount))
        else:
            self.progressbar.stop()
            self.loadingLabel.grid_forget()
            self.progressbar.grid_forget()
            self.downloadFinished=Label(self.downloadwindow,text="Download Completed",font=("Plaantagenet Cherokee",30))
            self.downloadFinished.grid(pady=(150,0))
            
            self.downloadLocation=Label(self.downloadwindow,text=self.yt.title,font=("Terminal",30))
            self.downloadLocation.grid(pady=(50,0))
            
            MB=float("%0.2f"%(self.maxFileSize/1000000))
            
            self.downloadedFileSize=Label(self.downloadwindow,text=str(MB)+" MB",font=("Vivaldi Italic",30))
            self.downloadedFileSize.grid(pady=(50,0))
             




if __name__=="__main__":
    window = Tk()
    window.state("zoomed")
    app=Application(window)
    window.mainloop()