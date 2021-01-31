import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込む
    newImage = PIL.Image.open(path).resize((300,300))
    #そのイメージをラベルに表示する
    imageDate = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageDate)
    imageLabel.image = imageDate
    

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)




root = tk.Tk()
root.geometry("400x350")

btn = tk.button(text="ファイルを開く",command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()


