import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class Crop:

    def __init__(self):
        self.video = ''
        self.Folder_Name = ''
        self.root = tk.Tk()
        self.root.title("Crop Video")
        self.root.geometry("350x400")  # set window
        self.root.columnconfigure(0, weight=1)  # set all content in center.
        # Ytd Link Label
        self.button = tk.Button(
            self.root, text="Choose video", command=self.openFile)
        self.button.grid()

        self.ytdError = tk.Label(self.root, text="", fg="red")
        self.ytdError.grid()

        self.ytdLabel = tk.Label(self.root, text="", fg="red")
        self.ytdLabel.grid()

        self.saveEntry = tk.Button(
            self.root, width=10, text="Choose Path", command=self.openLocation)
        self.saveEntry.grid()

        self.ytdLabelPath = tk.Label(
            self.root, text=self.Folder_Name, fg="red")
        self.ytdLabelPath.grid()

        # Ytd Link Label
        self.ytdLabelStart = tk.Label(self.root, text="Enter start")
        self.ytdLabelStart.grid()

        # Entry Box
        self.ytdEntryVarStart = tk.StringVar()
        self.ytdEntryStart = tk.Entry(
            self.root, width=50, textvariable=self.ytdEntryVarStart)
        self.ytdEntryStart.grid()

        # Ytd Link Label
        self.ytdLabelStop = tk.Label(self.root, text="Enter stop")
        self.ytdLabelStop.grid()

        # Entry Box
        self.ytdEntryVarStop = tk.StringVar()
        self.ytdEntryStop = tk.Entry(
            self.root, width=50, textvariable=self.ytdEntryVarStop)
        self.ytdEntryStop.grid()

        self.saveALabel = tk.Label(self.root, text="Save as")
        self.saveALabel.grid()

        self.saveAs = tk.StringVar()
        self.ytdEntrySave = tk.Entry(
            self.root, width=50, textvariable=self.saveAs)
        self.ytdEntrySave.grid()

        # Ytd Link Label
        self.buttonCrop = tk.Button(
            self.root, text="Crop video", command=self.cropVideo)
        self.buttonCrop.grid()

    def start(self):
        self.root.mainloop()

    def openLocation(self):
        self.Folder_Name = filedialog.askdirectory()
        self.ytdLabelPath.config(text=self.Folder_Name)


    def openFile(self):
        self.root.update()
        self.video = filedialog.askopenfilename(title='Choose file', filetypes=[
                                                ('All files', '*.*'), ("mp4 files", "*.mp4")])
        self.ytdError.config(text="Video path")
        self.ytdLabel.config(text=self.video)

    def getTotal(self, arr):
        copyArr = arr[:]
        copyArr.reverse()
        total = 0

        for i, val in enumerate(copyArr):
            if i == 0:
                total += int(val)
            if i == 1:
                total += int(val) * 60
            if i == 2:
                total += int(val) * 60 * 60

        return total

    def cropVideo(self):
        start = self.getTotal(self.ytdEntryStart.get().split(','))
        stop = self.getTotal(self.ytdEntryStop.get().split(','))
        saveAsName = self.Folder_Name + '/' + self.ytdEntrySave.get()
        ffmpeg_extract_subclip(self.video, start, stop,
                               targetname=saveAsName+".mp4")


if __name__ == "__main__":
    crop = Crop()

    crop.start()

