import tkinter as tk
from tkinter import ttk

from youtubetomp3 import youtube_to_mp3

class Convert(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube to MP3 Converter")
        self.geometry('300x50')
        self.url_link = tk.StringVar()
        self.youtube_link = ttk.Entry(textvariable=self.url_link, width=20)
        self.youtube_link.place(relx=0, rely=0.1)
        self.convert = ttk.Button(text='Convert', command=lambda: youtube_to_mp3(self.url_link.get()), width=6)
        self.convert.place(relx=0.65,rely=0.1)

    def paste(self):
        content = self.clipboard_get()
        self.url_link.set(content)


if __name__ == '__main__':
    app = Convert()
    app.mainloop()
