from tkinter import filedialog, messagebox
from tkinter import *
from PIL import Image
from sys import argv
from os import remove
import easyocr
from matplotlib import pyplot as plt
import pyperclip

def check(text):
    if text == "":
        messagebox.showerror("Error","Please scan an image first!")
        return True

def detectText(IMAGE_PATH):
    reader = easyocr.Reader([ 'en' ], gpu=True)
    result = reader.readtext(IMAGE_PATH)
    # print(result)

    # top_left = tuple(result[0][0][0])
    # bottom_right = tuple(result[0][0][2])
    text = ''

    for i in result:
        text+=f' {i[1]}'

    # text =  result[0][1]
    # font = cv2.FONT_HERSHEY_SIMPLEX

    # img = cv2.imread(IMAGE_PATH)
    # img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
    # img = cv2.putText(img,text,top_left,font,.5,(255,255,255), cv2.LINE_AA)
    # plt.imshow(img)
    # plt.show()
    print(text)
    return(text)

# detectText('C:\\Users\\Anurag\\Downloads\\handwritten1.jpg')

def getImagePath():
    root = Tk
    root.fileName = filedialog.askopenfilename(initialdir="/",title="Select your image",filetypes=(("jpeg files","*.jpg"),("png files","*.png")))
    return(root.fileName)



def copyText(textToBeCopied):
    if check(textToBeCopied) == True:
        return

    pyperclip.copy(textToBeCopied)
    messagebox.showinfo("Success","Text copied to clipboard!")



def saveFile(textToBeSaved):
    if check(textToBeSaved) == True:
        return

    root = Tk
    root.folderName = filedialog.asksaveasfilename(title="Save as", initialdir="/",initialfile="untitled", filetypes=((".txt","*.txt"),))
    print(root.folderName)
    with open(f"{root.folderName}.txt", "w") as file:
        file.write(f"{textToBeSaved}")

    messagebox.showinfo("Success","File saved successfully!")



def toDoc(textToBeWritten):
    if check(textToBeWritten) == True:
        return

    tempFilePath = "D:\\PROGRAMMING\\ALL CODES\\CODES NEW\\Python\\MinorProjectOCR\\temp\\temp.txt"
    
    with open(tempFilePath,"w") as tempFile:
        tempFile.write(f"{textToBeWritten}")
    

    try:
        txt=open(argv[1], "r")
    except IndexError:
        print("No file entered. Using default file...")
        txt=open(tempFilePath, "r")
    except FileNotFoundError:
        print("Could not find file. Using default file...")
        txt=open(tempFilePath, "r")  

    BG = Image.open("D:\\PROGRAMMING\\ALL CODES\\CODES NEW\\Python\\MinorProjectOCR\\Images\\page.png")
    sheet_width=BG.width
    gap, ht = 0, 0

    for i in txt.read().replace("\n",""):
        cases = Image.open("D:\\PROGRAMMING\\ALL CODES\\CODES NEW\\Python\\MinorProjectOCR\\Letters\\{}.png".format(str(ord(i))))
        BG.paste(cases, (gap, ht),mask=cases)
        size = cases.width
        height=cases.height
        gap+=size

        if sheet_width < gap or len(i)*115 >(sheet_width-gap):
            gap,ht=0,ht+140
    
    # BG.show()
    root = Tk
    root.folderName = filedialog.asksaveasfilename(title="Save image as", initialdir="/", initialfile="untitled")
    print(root.folderName)
    BG.save(f"{root.folderName}.png")