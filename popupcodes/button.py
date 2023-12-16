import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

#new window
def on_button_click():
    new_window = tk.Toplevel(root)
    new_window.title("Farm")
    label = tk.Label(new_window, text="Welcome to the farm!")
    label.pack(padx=20, pady=20)


#button
root = tk.Tk()
root.title("Click here!")
button = tk.Button(root, text="Error⚠️", command=on_button_click)
button.pack(pady=10)
root.mainloop()