import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from operations import toDoc
from qrCodeFunc import toQrCode

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Note To Document")
        self.root.geometry("600x600")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, font=("Helvetica", 12), bg="#E6DEFF")
        self.text_area.pack(fill="both", expand=True)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)

        # Create file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_command(label="Convert to Doc", command=self.convert)
        self.menu_bar.add_command(label="Convert to QR", command=self.toQR)

        # Add menu bar to the root window
        self.root.config(menu=self.menu_bar)

    def convert(self):
        text = self.text_area.get("1.0", "end-1c")
        toDoc(text)
    
    def toQR(self):
        text = self.text_area.get("1.0", "end-1c")
        toQrCode(text)

    def new_file(self):
        self.root.title("Notepad")
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = askopenfilename(defaultextension=".txt",
                                    filetypes=[("Text Files", "*.txt"),
                                               ("All Files", "*.*")])
        if file_path:
            self.root.title(f"Notepad - {file_path}")
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        file_path = asksaveasfilename(defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"),
                                                 ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

def launchNotepad():
    root = tk.Toplevel()
    notepad = Notepad(root)
    root.mainloop()
