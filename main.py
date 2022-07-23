# import packages
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import os

from pytube import YouTube

# * FUNCTIONS *


def reset():
    # set link_input state to enabled
    link_input.config(state=NORMAL)

    # set get video button state to enabled
    get_video_btn .config(state=NORMAL)

    # set video thumbnail button state to disabled
    video_thumbnail_btn.config(state=DISABLED)

    # set download button state to disabled
    download_btn.config(state=DISABLED)

    # clear the link_input value
    link_input.delete(0, END)
    # clear the video_title value
    video_title_input.delete(0, END)


def get_video_obj():
    # get the link from the link_input
    link = link_input.get()

    # create a YouTube object
    video = YouTube(link)

    return video


def open_thumbnail():
    # get the video object
    video = get_video_obj()

    # get the video thumbnail url
    url = video.thumbnail_url

    # open the url in the default browser
    webbrowser.open(url)


def get_video():
    # get the video object
    video = get_video_obj()

    # set the video title to the video_title_input
    video_title_input.insert(0, video.title)

    # set the link_input state to disabled
    link_input.config(state=DISABLED)

    # set get video button state to disabled
    get_video_btn.config(state=DISABLED)

    # set video thumbnail button state to enabled
    video_thumbnail_btn.config(state=NORMAL)

    # set download button state to enabled
    download_btn.config(state=NORMAL)


def download_video():
    # get the video object
    video = get_video_obj()

    # get the video stream with highest resolution (usually 720p)
    video_stream = video.streams.filter(
        progressive=True).order_by('resolution').desc().first()

    # check if there's a directory called 'videos'
    if not os.path.exists('videos'):
        # if not, create one
        os.makedirs('videos')

    # download and move the downloaded video to the 'videos' directory
    video_stream.download('videos')

    # show a message box
    messagebox.showinfo("Success", "Download Completed")


# * CREATE WINDOW *
root = Tk()
root.title("YouTube Downloader")
root.geometry("600x500")
root.resizable(False, False)
root.configure(background='black')


# title label
title_label = Label(root, text="YouTube Video Downloader", font=(
    "Helvetica", 20), foreground="white", background="black")
title_label.pack(pady=30)

# label border
title_label.config(borderwidth=3, relief="groove")


# * FRAME *
frame = Frame(root, background="black", width=400, height=300)
frame.pack(pady=1)

# frame border
frame.config(borderwidth=3, relief="groove")

# * CONTENT INSIDE FRAME *

# link label + input box
link_label = Label(frame, text="Link:", font=(
    "Helvetica", 15), foreground="white", background="black")
link_label.grid(row=0, column=0, padx=10, pady=10)


link_input = Entry(frame, font=("Helvetica", 15),
                   foreground="white", background="black", justify="center")
link_input.grid(row=0, column=1, padx=10, pady=10)


# create three buttons next to each other
get_video_btn = Button(frame, text="Get Video", font=(
    "Helvetica", 15), foreground="white", background="black", command=get_video)
get_video_btn.grid(row=1, column=0, padx=10, pady=10)


reset_btn = Button(frame, text="Reset", font=(
    "Helvetica", 15), foreground="white", background="black", command=reset)
reset_btn.grid(row=1, column=1, padx=10, pady=10)

# make a line separating
line = Label(frame, text="-----------------------------------------------------",
             font=("Helvetica", 15), foreground="white", background="black")
line.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# * video information *

# video title label
video_title_label = Label(frame, text="Title:", font=(
    "Helvetica", 15), foreground="white", background="black")
video_title_label.grid(row=3, column=0, padx=10, pady=10)

# video input box (used to show information)
video_title_input = Entry(frame, font=("Helvetica", 15),
                          foreground="white", background="black", justify="center")
video_title_input.grid(row=3, column=1, padx=10, pady=10)

# video thumbnail label
video_thumbnail_label = Label(frame, text="Thumbnail:", font=(
    "Helvetica", 15), foreground="white", background="black")
video_thumbnail_label.grid(row=4, column=0, padx=10, pady=10)

# video thumbnail button
video_thumbnail_btn = Button(frame, text="Open on browser", font=(
    "Helvetica", 15), foreground="white", background="black", state="disabled", command=open_thumbnail)
video_thumbnail_btn.grid(row=4, column=1, padx=10, pady=10)


# make a line separating
line1 = Label(frame, text="-----------------------------------------------------",
              font=("Helvetica", 15), foreground="white", background="black")
line1.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# centered download button
download_btn = Button(frame, text="Download", font=(
    "Helvetica", 15), foreground="white", background="black", state="disabled", command=download_video)
download_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# info button on bottom right corner
info_btn = Button(frame, fg='black', background='grey',
                  relief='flat', bitmap='info', width=20, height=20, command=lambda: webbrowser.open(
                      "https://github.com/TiagoRibeiro25/YoutubeVideoDownloader"))
info_btn.place(x=371, y=350)

# * END OF CONTENT INSIDE FRAME *


root.mainloop()
