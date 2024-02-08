# @author Kelsey Kopper
import sys
import string
import cipher as c
import tkinter as tk

from tkinter import filedialog 
from tkinter import messagebox

# if __name__ == '__main__':
#   c_map = c.CipherMap("hw1")
#   c_map.create_cipher()
#   c_map.code_file("tests/hw1.txt", "encrypt")

def open_file():
  path = filedialog.askopenfilename() 
  if not path: 
    return 
  with open(path, "r") as file: 
    text = file.read()
    text_edit.insert(tk.END, text)

window = tk.Tk() 
window.title("Cipher program")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

text_edit = tk.Text(window)

window.mainloop()