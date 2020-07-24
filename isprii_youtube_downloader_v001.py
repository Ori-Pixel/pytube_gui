#!/usr/bin/env python
# coding: utf-8

# In[96]:


from pytube import YouTube
#import pkg_resources.py2_warn
import tkinter as tk
import os
import PIL
from PIL import Image, ImageTk
import requests
from io import BytesIO
from tkinter import filedialog

# from the tkinter library 
from tkinter import *
   
# import filedialog module 
import tkinter.filedialog as fd

class SampleApp(tk.Tk):
    def __init__(self):
        video_test = ""
        tk.Tk.__init__(self)
        self.youtube_url_entry = tk.Entry(self, width=75)
        self.file_path_entry = tk.Entry(self, width=75)
        self.download_button = tk.Button(self, text="Load Video Quality", command=self.on_button)
        self.file_browser_button = tk.Button(self, text="Browse File Location", command=self.file_browse)
        self.download_button.pack()
        self.youtube_url_entry.pack()
        self.file_browser_button.pack()
        self.file_path_entry.pack()
        self.tempdir = os.getcwd()
    
    def on_button(self):
        try:
            yt = YouTube(self.youtube_url_entry.get())
            self.streams = yt.streams
            self.top = Toplevel() 
            self.top.geometry("800x700")
            self.top.title("Please select a video grade") 

            btn = [] #creates list to store the buttons ins
            for i in range(0, len(self.streams)): #this says for *counter* in *however many elements there are in the list files*
                btn.append(Button(self.top, text=self.streams[i], command=lambda c=i: SampleApp.select_video(self, btn[c].cget("text"))))
                btn[i].pack() #this packs the buttons
            self.download_now = tk.Button(self, text="Click Here to Download", command=self.download_video)
            self.download_now.pack()
            
            
        except:
            print("Either incorrect video url, video is geolocation locked, or it is unavailable")
    
    def select_video(self, video_test):
        self.top.destroy()
        if "itag" in video_test:
            video_id_after = video_test.split('''itag="''')[1]
            self.video_id = video_id_after.split('''"''')[0]
        else:
            print('''This video does not have a corresponding ID''')
        return self.video_id
    
    def file_browse(self):
        currdir = os.getcwd()
        self.tempdir = fd.askdirectory(initialdir=currdir, title='Please select a directory')
        self.file_path_entry.insert(0, self.tempdir)
        return self.tempdir
    
    def download_video(self):
        stream = self.streams.get_by_itag(self.video_id)
        self.download_now.destroy()
        stream.download(self.tempdir)
        return


   
    

    
app = SampleApp()
app.title('ISPRII Youtube Downloader')
app.geometry("500x200")
app.mainloop()

