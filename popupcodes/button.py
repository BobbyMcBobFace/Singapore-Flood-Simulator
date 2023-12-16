import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    print("Button Clicked!")

root = tk.Tk()
root.title("Button with Image")

# Load and resize the image for the button
image_path = ""  # Replace with the path to your image file
image = Image.open(image_path)
image = image.resize((100, 50))  # Adjust the size as needed
photo_image = ImageTk.PhotoImage(image)

# Create a button with the custom image
button = tk.Button(root, image=photo_image, command=on_button_click, bd=0, highlightthickness=0)

# Pack the button to display it
button.pack(pady=10)

root.mainloop()

  
