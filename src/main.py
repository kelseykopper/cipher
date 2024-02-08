# @author Kelsey Kopper
import sys
import string
import cipher as c
import tkinter as tk

from tkinter import filedialog 
from tkinter import messagebox
from tkinter import ttk

# if __name__ == '__main__':
#   c_map = c.CipherMap("hw1")
#   c_map.create_cipher()
#   c_map.code_file("tests/hw1.txt", "encrypt")

# really only need a couple pieces of info from ui:
# mode -> encrypt or decrypt (maybe have selection option for this)
# cipher lib name -> text box
  # should program automatically search for lib with this name? 
  # maybe then if it doesn't find a lib with that name, generate new one
# file to encode/decode

def open_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    txt_display.config(state=tk.NORMAL)  # Temporarily enable the widget to modify its content
    txt_display.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_display.insert(tk.END, text)
    txt_display.config(state=tk.DISABLED)  # Disable the widget to make it read-only
    window.title(f"Cipher - {filepath}")

window = tk.Tk()
window.title("Cipher")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

textrow = 0

# window for displaying the opened file
txt_display = tk.Text(window)
txt_display.config(state=tk.DISABLED)  # Start with the widget in the disabled state
txt_display.grid(row=0, column=1, sticky="nsew")

menu_frame = tk.Frame(window, relief=tk.RAISED, bd=2)
menu_frame.grid(row=0, column=0, sticky="ns")
menu_frame.grid_rowconfigure(index=0, minsize=20)

# open file prompt
ttk.Label(menu_frame, text="Select file to encode/decode").grid(column=0, row=textrow, sticky="w", pady=(10,0))
textrow += 1

# buttons
open_button = tk.Button(menu_frame, text="Open", command=open_file, bd=10)
open_button.grid(row=textrow, column=0, sticky="ew", padx=20, pady=(0,25))
textrow += 2

# prompt to enter cipher lib name
ttk.Label(menu_frame, text="Enter the name of the cipher library").grid(column=0, row=textrow, sticky="w")
textrow += 1

# text box to input cipher lib name
cipher_lib = tk.StringVar()
lib_entry = ttk.Entry(menu_frame, width=30, textvariable=cipher_lib)
lib_entry.grid(column=0, row=textrow, sticky="ew", padx=20, pady=(0,25))
textrow += 2

# prompt to choose mode 
ttk.Label(menu_frame, text="Select mode:").grid(column=0, row=textrow, sticky="w")
textrow += 1

# option to select between encoding and decoding
mode = tk.StringVar()
encode_button = tk.Radiobutton(menu_frame, text="encode", variable=mode, value="encode")
decode_button = tk.Radiobutton(menu_frame, text="decode", variable=mode, value="decode")

encode_button.grid(row=textrow, column=0, sticky="w", padx=20)
textrow += 1
decode_button.grid(row=textrow, column=0, sticky="w", padx=20, pady=(0,25))
textrow += 2

# button to convert; TODO - add command functionality
code_button = tk.Button(menu_frame, text="GO")
code_button.grid(row=textrow, column=0, sticky="ew", padx=20, pady=(5, 20))

window.mainloop()
