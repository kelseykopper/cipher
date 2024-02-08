import tkinter as tk

def selection_made():
    choice = choice_var.get()  # Get the current value of choice_var
    # Update label text based on the choice
    label.config(text=f"You selected: {choice}")

window = tk.Tk()
window.title("Select an Option")

# Variable to keep track of the selected option
choice_var = tk.StringVar(value="Option 1")  # Default value

# Create two radio buttons for the options
rb1 = tk.Radiobutton(window, text="Option 1", variable=choice_var, value="Option 1", command=selection_made)
rb2 = tk.Radiobutton(window, text="Option 2", variable=choice_var, value="Option 2", command=selection_made)

# Label to display the selected option
label = tk.Label(window, text="You selected: Option 1")

# Positioning the widgets
rb1.pack()
rb2.pack()
label.pack()

window.mainloop()