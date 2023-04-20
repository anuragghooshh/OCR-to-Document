from tkinter import *
from PIL import Image

def showSplash():
    root = Tk()
    root.overrideredirect(True)
    root.geometry("200x200")
    root.eval('tk::PlaceWindow . center')
    root.resizable(False,False)

    canvas = Canvas(
        root,
        bg = "#2935AB",
        height = 200,
        width = 200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",
    )
    canvas.place(x=0,y=0)

    imagePath = r'D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\v2\splash.gif'
    splashAnimationGIF = Image.open(imagePath)
    splashAnimationGIF.resize = False

    frames = splashAnimationGIF.n_frames
    imageObject = [PhotoImage(file=imagePath, format=f'gif -index {i}') for i in range(frames)]

    count = 0
    showAnimation = None

    def animation(count):
        global showAnimation
        newImage = imageObject[count]

        gif_Label.configure(image=newImage)
        count+=1
        if count == (frames-1):
            root.destroy()
            return

        showAnimation = root.after(40,lambda: animation(count))

    gif_Label = Label(root, image="")
    gif_Label.place(x=50,y=50, height=100, width=100)

    animation(count)

    root.mainloop()
