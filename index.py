import tkinter as tk
from tkinter import ttk,filedialog
import pytube
import os
import ffmpeg

class Downloader:

    def __init__(self):
        self.Folder_Name = ""
        self.choices = ["Video", "Audio"]

        self.root = tk.Tk()
        self.root.title("YTD Downloader")
        self.root.geometry("350x400")  # set window
        self.root.columnconfigure(0, weight=1)  # set all content in center.

        # Ytd Link Label
        self.ytdLabel = tk.Label(self.root, text="Enter the URL of the Video")
        self.ytdLabel.grid()

        # Entry Box
        self.ytdEntryVar = tk.StringVar()
        self.ytdEntry = tk.Entry(self.root, width=50, textvariable=self.ytdEntryVar)
        self.ytdEntry.grid()

        # Error Msg
        self.ytdError = tk.Label(self.root, text="", fg="red")
        self.ytdError.grid()

        # btn of save file
        self.saveEntry = tk.Button(self.root, width=10, text="Choose Path", command=self.openLocation)
        self.saveEntry.grid()

        # Error Msg location
        self.locationError = tk.Label(self.root, text="", fg="red")
        self.locationError.grid()

        # Download Quality
        self.ytdQuality = tk.Label(self.root, text="Select Option")
        self.ytdQuality.grid()

        # combobox
        self.ytdchoices = ttk.Combobox(self.root, values=self.choices)
        self.ytdchoices.grid()

        # donwload btn
        self.downloadbtn = tk.Button(self.root, text="Download", command=self.downloadVideo)
        self.downloadbtn.grid()

        # developer Label
        self.developerlabel = tk.Label(self.root, text="Dream Developers")
        self.developerlabel.grid()

    def openLocation(self):
        self.Folder_Name = filedialog.askdirectory()
        if(len(self.Folder_Name) > 1):
            self.locationError.config(text=self.Folder_Name, fg="green")
        else:
            self.locationError.config(text="Please Choose Folder!!", fg="red")


    def downloadVideo(self):
        choice = self.ytdchoices.get()
        urls = self.ytdEntry.get().split(',')

        for url in urls:
            validUrl = url.strip()
            if 'list' not in validUrl:
                if(len(validUrl) > 0):
                    self.download(validUrl, choice)
                    self.ytdError.config(text="Download Completed!!")
            else:
                playlist = pytube.Playlist(validUrl)
                for playlistUrl in playlist:
                    self.download(playlistUrl, choice)

                self.ytdError.config(text="Download Completed!!")

    def download(self, url, choice):
        self.ytdError.config(text="")
        yt = pytube.YouTube(str(url))

        if(choice == self.choices[0]):
            select = yt.streams.filter(progressive=True).order_by(
                'resolution').desc().first()

        elif(choice == self.choices[1]):
            select = yt.streams.filter(
                only_audio=True, mime_type="audio/mp4").order_by('abr').desc().first()

        self.select.download(self.Folder_Name)
        name = self.select.default_filename

        if choice == self.choices[1]:
            path = os.path.join(self.Folder_Name+'/'+name)
            name = name.split('.mp4')[0] + '.mp3'
            path2 = os.path.join(self.Folder_Name+'/'+name)
            (ffmpeg.input(path).output(path2).run())
            os.remove(path)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    downloader = Downloader()

    downloader.start()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework':'tcl' part_manager.py
# '''

