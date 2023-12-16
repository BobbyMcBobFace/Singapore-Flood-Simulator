import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    print("Button Clicked!")

def display_combined_map_and_button(map_image_path, button_image_path, button_x, button_y):
    root = tk.Tk()
    root.title("Combined Example")

    # Load and resize the map image
    map_image = Image.open(map_image_path)
    map_image = map_image.resize((1000, 1000))
    map_photo_image = ImageTk.PhotoImage(map_image)

    # Create a canvas for the map image
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=map_photo_image)

    # Load and resize the button image
    button_image = Image.open(button_image_path)
    button_image = button_image.resize((70, 35))
    button_photo_image = ImageTk.PhotoImage(button_image)

    # Create the button on the canvas with specified coordinates
    button = tk.Button(root, image=button_photo_image, command=on_button_click, bd=0, highlightthickness=0)
    canvas.create_window(button_x, button_y, anchor="center", window=button)

    root.mainloop()

# Provide paths to your image files
map_image_path = "./popupcodes/hi.jpeg"
button_image_path = "./popupcodes/Farm.png"

# Specify the initial coordinates for the button
initial_button_x = 300
initial_button_y = 500

# Call the function to display the combined map and button with initial coordinates
display_combined_map_and_button(map_image_path, button_image_path, initial_button_x, initial_button_y)




