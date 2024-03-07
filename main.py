import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        messagebox.showinfo("Download", "Downloading video...")
        stream.download()
        messagebox.showinfo("Download", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Create main application window
app = tk.Tk()
app.title("YouTube Video Downloader")

# Create URL entry field
url_label = tk.Label(app, text="Enter YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(app, width=50)
url_entry.pack()

# Create download button
download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack()

# Run the application
app.mainloop()
