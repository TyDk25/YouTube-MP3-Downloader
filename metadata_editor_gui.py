import tkinter as tk
from tkinter import ttk, filedialog
from mp3_file_handler import MusicHandler
from tkinter import messagebox
from pathlib import Path

m = MusicHandler()


class MetaData(tk.Tk):

    """
    tkinter GUI that handles editing metadata.
    """
    def __init__(self):
        super().__init__()
        self.title("MetaData Editor")
        self.geometry('450x350')

        self.filepath_text = tk.StringVar()
        self.title_text = tk.StringVar()
        self.artist_text = tk.StringVar()
        self.album_text = tk.StringVar()
        self.track_number_text = tk.StringVar()
        self.album_art_text = tk.StringVar()

        self.filepath = ttk.Button(text='Filepath:', width=8, command=lambda: self.get_filepath())
        self.filepath.place(relx=0, rely=0.01)
        self.title_label = ttk.Label(text='Enter Title: ')
        self.title_label.place(relx=0.01, rely=0.135)

        self.artist_label = ttk.Label(text='Enter Artist: ')
        self.artist_label.place(relx=0.01, rely=0.27)

        self.album_label = ttk.Label(text='Enter Album: ')
        self.album_label.place(relx=0.01, rely=0.4)

        self.album_art_label = ttk.Label(text='Enter Album Art: ')
        self.album_art_label.place(relx=0.01, rely=0.55)

        self.track_number_label = ttk.Label(text='Enter Track: ')
        self.track_number_label.place(relx=0.01, rely=0.7)

        self.metadata_button = ttk.Button(text='Edit Metadata', width=15, command=lambda: self.metadata())
        self.metadata_button.place(relx=0.3, rely=0.85)

        self.filepath_entry = ttk.Entry(textvariable=self.filepath_text, width=30)
        self.filepath_entry.place(relx=0.3, rely=0.01)

        self.title_entry = ttk.Entry(textvariable=self.title_text, width=30)
        self.title_entry.place(relx=0.3, rely=0.13)

        self.artist_entry = ttk.Entry(textvariable=self.artist_text, width=30)
        self.artist_entry.place(relx=0.3, rely=0.27)

        self.album_entry = ttk.Entry(textvariable=self.album_text, width=30)
        self.album_entry.place(relx=0.3, rely=0.4)

        self.album_art_entry = ttk.Entry(textvariable=self.album_art_text, width=30)
        self.album_art_entry.place(relx=0.3, rely=0.55)

        self.track_entry = ttk.Entry(textvariable=self.track_number_text, width=30)
        self.track_entry.place(relx=0.3, rely=0.7)

        self.bind('<Control-v>', lambda event: self.paste())
        self.bind('<Command-v>', lambda event: self.paste())

    def get_filepath(self):
        path = filedialog.askopenfilename(filetypes=[('MP3 files', '*.mp3')])
        self.filepath_text.set(path)

    def metadata(self):
        data = {
            'Title': self.title_text.get(),
            'Artist': self.artist_text.get(),
            'Album': self.album_text.get(),
            'Track Number': self.track_number_text.get(),
            'Album Art': self.album_art_text.get()
        }
        m.meta_data(self.filepath_text.get(), data)
        messagebox.showinfo("Metadata", f'{Path(self.filepath_text.get()).stem} details changed successfully!')

    def paste(self):
        content = self.clipboard_get()
        self.album_art_text.set(content)


if __name__ == '__main__':
    app = MetaData()
    app.mainloop()
