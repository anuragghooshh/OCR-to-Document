from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x600")
window.configure(bg = "#eeeeee")
canvas = Canvas(
    window,
    bg = "#eeeeee",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\\background.png")
background = canvas.create_image(
    0, 0,
    image=background_img)

canvas.create_text(
    -248.0, 38.0,
    text = "Please choose an image",
    fill = "#eeeeee",
    font = ("Tahoma-Bold", int(20.0)))

canvas.create_text(
    -232.0, 142.0,
    text = "Text detected successfully!",
    fill = "#eeeeee",
    font = ("Tahoma-Bold", int(20.0)))

img0 = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 112, y = 78,
    width = 100,
    height = 32)

img1 = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 232, y = 78,
    width = 100,
    height = 32)

img2 = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = -368, y = 197,
    width = 100,
    height = 32)

img3 = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = -248, y = 197,
    width = 100,
    height = 32)

img4 = PhotoImage(file = f"D:\PROGRAMMING\ALL CODES\CODES NEW\Python\MinorProjectOCR\GUI\img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = -128, y = 197,
    width = 100,
    height = 32)

window.resizable(False, False)
window.mainloop()
