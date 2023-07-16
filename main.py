from pytube import YouTube
import os
from tkinter import filedialog, messagebox
from tkinter import *

window=Tk()
window.title("PyTube2Mp4")
window.geometry("500x200")
window.resizable(0, 0)

def outfilefunc():
    global out
    out=filedialog.askdirectory()
    outpath=Label(text=out)
    outpath.place(x=100, y=55)

def downloadfunc():
    global out
    restest=resvar.get()
    test=vartype.get()
    if restest==1:
        restest="144p"
    if restest==2:
        restest="360p"
    if restest==3:
        restest="480p"
    if restest==4:
        restest="720p"
    if restest==5:
        restest="1080p"
    if test==1 and restest!=0:
        yt=YouTube(link.get())
        video=yt.streams.filter(res=restest, progressive=True).first()
        try:
            outfile=video.download(output_path=out)
            base, ext=os.path.splitext(outfile)
            newfile=base+".mp4"
            os.rename(outfile, newfile)
            messagebox.showinfo('PyTube2Mp4 Completed', yt.title+" has downloaded succesfully!")
        except:
            messagebox.showerror('PyTube2Mp4 Error', "This resolution isn't available!")
    elif test==2:
        yt=YouTube(link.get())
        video=yt.streams.filter(only_audio=True).first()
        try:
            outfile=video.download(output_path=out)
            base, ext=os.path.splitext(outfile)
            newfile=base+".m4a"
            os.rename(outfile, newfile)
            messagebox.showinfo('PyTube2Mp4 Completed', yt.title+" has downloaded succesfully!")
        except:
            messagebox.showerror('PyTube2Mp4 Error', 'Unknoun error! Please try again later!')
    else:
        messagebox.showwarning('PyTube2Mp4 Error', 'Please check the type of file and the resolution!')

linktext=Label(text="Youtube Link: ")
linktext.place(x=20, y=20)
link=Entry(width=50)
link.place(x=100, y=20)

chooseoutpath=Button(text="Output: ", command=outfilefunc)
chooseoutpath.place(x=20, y=50)

download=Button(text="Download", command=downloadfunc)
download.place(x=50, y=150)

vartype=IntVar()
mp3=Radiobutton(text="MP4", variable=vartype, value=1)
mp3.place(x=30, y=100)
mp3=Radiobutton(text="M4A", variable=vartype, value=2)
mp3.place(x=90, y=100)

restext=Label(text="Choose resolution (only required for mp4):")
restext.place(x=200, y=90)
resvar=IntVar()
low=Radiobutton(text="144p", variable=resvar, value=1)
low.place(x=250, y=110)
lowmed=Radiobutton(text="360p", variable=resvar, value=2)
lowmed.place(x=250, y=130)
med=Radiobutton(text="480p", variable=resvar, value=3)
med.place(x=250, y=150)
medhigh=Radiobutton(text="720p", variable=resvar, value=4)
medhigh.place(x=300, y=110)
high=Radiobutton(text="1080p", variable=resvar, value=5)
high.place(x=300, y=130)

window.mainloop()