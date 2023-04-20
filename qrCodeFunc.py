import tkinter as tk
from PIL import Image, ImageTk
import qrcode
from operations import check

def toQrCode(detectedText:str):
    if check(detectedText) == True:
        return
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    
    qr.add_data(f"{detectedText}")
    qrCode = qr.make_image(fill_color="black", back_color="white")
    qrCode = qrCode.resize((300, 300), Image.ANTIALIAS)

    qrRoot = tk.Toplevel()

    # Root window customization
    qrRoot.title("QR Code")
    qrRoot.resizable(False,False)

    # Centering
    screen_width = qrRoot.winfo_screenwidth()
    screen_height = qrRoot.winfo_screenheight()

    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (300/2)
    qrRoot.geometry(f'300x300+{int(x)}+{int(y)}')

    img = ImageTk.PhotoImage(qrCode)
    panel = tk.Label(qrRoot,image=img)
    panel.image = img
    panel.pack(side="bottom", fill="both", expand="yes")
