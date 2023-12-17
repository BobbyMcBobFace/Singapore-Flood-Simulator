from tkinter import Tk, Canvas
from PIL import Image, ImageTk

class StaticImage:
    def __init__(self, canvas, image_path, initial_x, initial_y, size=(200, 200)):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.image_id = canvas.create_image(initial_x, initial_y, anchor="nw", image=self.photo_image)

class DraggableImage:
    def __init__(self, canvas, image_path, initial_x, initial_y, size=(200, 200)):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.image_id = canvas.create_image(initial_x, initial_y, anchor="nw", image=self.photo_image)

        # Bind mouse events for dragging
        canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.on_press)
        canvas.tag_bind(self.image_id, "<B1-Motion>", self.on_drag)

        self.last_x = 0
        self.last_y = 0

    def on_press(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_drag(self, event):
        delta_x = event.x - self.last_x
        delta_y = event.y - self.last_y
        self.canvas.move(self.image_id, delta_x, delta_y)
        self.last_x = event.x
        self.last_y = event.y

def display_combined_images(static_image_paths, draggable_image_paths):
    root = Tk()
    root.title("Combined Image Example")

    canvas = Canvas(root, width=900, height=750)
    canvas.pack()

    # Create StaticImage instances for each image
    static_image1 = StaticImage(canvas, static_image_paths[0], 150, 500)
    static_image2 = StaticImage(canvas, static_image_paths[1], 300, 500)
    static_image3 = StaticImage(canvas, static_image_paths[2], 450, 500)

    # Create DraggableImage instances for each image
    draggable_image1 = DraggableImage(canvas, draggable_image_paths[0], 300, 100)
    draggable_image2 = DraggableImage(canvas, draggable_image_paths[1], 450, 100)
    draggable_image3 = DraggableImage(canvas, draggable_image_paths[2], 150, 100)

    root.mainloop()

# Provide paths to your image files
static_image_paths = ["./popupcodes/strawpot.png", "./popupcodes/applepot.png", "./popupcodes/orangepot.png"]
draggable_image_paths = ["./popupcodes/StrawSeeds.png", "./popupcodes/appleseeds.png", "./popupcodes/orangeseeds.png"]

# Call the function to display both static and draggable images on one screen
display_combined_images(static_image_paths, draggable_image_paths)





























import tkinter as tk
from PIL import Image, ImageTk
import pygame
import threading

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 1000

# Tkinter root window
root = tk.Tk()
root.title("Game Interface")

# Set up colors
green = (152, 245, 255)
blue = (69, 139, 0)

# Set up the stat bar dimensions
bar_width = 400
bar_height = 20

# Set up the font
font = ("Arial", 16)

# Initial water status
water_current = 69
water_max = 100

food_current = 69
food_max = 100

# Function to draw the water status bar and label
def draw_water_status():
    # Draw the water stat bar at the top
    bar_fill_width = int(bar_width * (water_current / water_max))
    canvas.create_rectangle((width - bar_width) // 2, 10, (width - bar_width) // 2 + bar_fill_width, 10 + bar_height, fill=green)

    # Display the water status label
    water_label.config(text="Water: {}/{}".format(water_current, water_max))

# Function to draw the food status bar and label
def draw_food_status():
    # Draw the food stat bar at the top
    bar_fill_width = int(bar_width * (food_current / food_max))
    canvas.create_rectangle((width - bar_width) // 2, 40, (width - bar_width) // 2 + bar_fill_width, 40 + bar_height, fill=blue)

    # Display the food status label
    food_label.config(text="Food: {}/{}".format(food_current, food_max))

# Main game loop
def update_statuses():
    while True:
        # Update the water and food status bars
        draw_water_status()
        draw_food_status()

        # Update the Tkinter window
        root.update()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

# Function to handle button clicks
def on_button_click(background_image_path):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Load and resize the background image for the button
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((800, 600))
    background_photo_image = ImageTk.PhotoImage(background_image)

    # Create a label for the background image
    background_label = tk.Label(new_window, image=background_photo_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Keep a reference to the image to prevent garbage collection
    new_window.background_photo_image = background_photo_image

# Create a canvas for drawing
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Load and resize the map image
map_image_path = "./popupcodes/hi.jpeg"
map_image = Image.open(map_image_path)
map_image = map_image.resize((1000, 1000))
map_photo_image = ImageTk.PhotoImage(map_image)

# Create a canvas for the map image
canvas.create_image(0, 0, anchor="nw", image=map_photo_image)

# Load and resize the ship image
ship_image_path = "./popupcodes/Ship.png"
ship_image = Image.open(ship_image_path)
ship_image = ship_image.resize((150, 150))
ship_photo_image = ImageTk.PhotoImage(ship_image)

# Create a canvas for the ship image
ship_canvas = canvas.create_image(650, 650, anchor="center", image=ship_photo_image)

# Load and resize the second aesthetic picture (Cargo.png)
cargo_image_path = "./popupcodes/Cargo.png"
cargo_image = Image.open(cargo_image_path)
cargo_image = cargo_image.resize((200, 200))
cargo_photo_image = ImageTk.PhotoImage(cargo_image)

# Create a canvas for the second aesthetic picture
cargo_canvas = canvas.create_image(150, 670, anchor="center", image=cargo_photo_image)

# Load and resize the third aesthetic picture (Airport.png)
airport_image_path = "./popupcodes/Airport.png"
airport_image = Image.open(airport_image_path)
airport_image = airport_image.resize((200, 200))
airport_photo_image = ImageTk.PhotoImage(airport_image)

# Create a canvas for the third aesthetic picture
airport_canvas = canvas.create_image(750, 500, anchor="center", image=airport_photo_image)

# Display the water and food status labels
water_label = tk.Label(root, text="Water: {}/{}".format(water_current, water_max), font=font)
water_label.place(x=10, y=10)

food_label = tk.Label(root, text="Food: {}/{}".format(food_current, food_max), font=font)
food_label.place(x=10, y=40)

# Load and resize the first button image
button_image_path = "./popupcodes/Wheat.png"  # Change this path accordingly
button_image = Image.open(button_image_path)
button_image = button_image.resize((40, 40))
button_photo_image = ImageTk.PhotoImage(button_image)

# Create the first button on the canvas with specified coordinates
first_button = tk.Button(root, image=button_photo_image, command=lambda: on_button_click("./popupcodes/Farm.png"), bd=0, highlightthickness=0)
first_button_x = 200
first_button_y = 500
canvas.create_window(first_button_x, first_button_y, anchor="center", window=first_button)

# Load and resize the second button image
second_button_image_path = "./popupcodes/Water.png"
second_button_image = Image.open(second_button_image_path)
second_button_image = second_button_image.resize((40, 40))
second_button_photo_image = ImageTk.PhotoImage(second_button_image)

# Create the second button on the canvas with specified coordinates
second_button = tk.Button(root, image=second_button_photo_image, command=lambda: on_button_click("./popupcodes/WaterPump.png"), bd=0, highlightthickness=0)
second_button_x = 330
second_button_y = 390
canvas.create_window(second_button_x, second_button_y, anchor="center", window=second_button)

# Load and resize the third button image
third_button_image_path = "./popupcodes/Wheat.png"  # Change this path accordingly
third_button_image = Image.open(third_button_image_path)
third_button_image = third_button_image.resize((40, 40))
third_button_photo_image = ImageTk.PhotoImage(third_button_image)

# Create the third button on the canvas with specified coordinates
third_button = tk.Button(root, image=third_button_photo_image, command=lambda: on_button_click("./popupcodes/Farm.png"), bd=0, highlightthickness=0)
third_button_x = 240  # Adjust the x-coordinate as needed
third_button_y = 420  # Adjust the y-coordinate as needed
canvas.create_window(third_button_x, third_button_y, anchor="center", window=third_button)

# Load and resize the fourth button image (duplicate of the first and third)
fourth_button_image_path = "./popupcodes/Wheat.png"  # Change this path accordingly
fourth_button_image = Image.open(fourth_button_image_path)
fourth_button_image = fourth_button_image.resize((40, 40))
fourth_button_photo_image = ImageTk.PhotoImage(fourth_button_image)

# Create the fourth button on the canvas with specified coordinates
fourth_button = tk.Button(root, image=fourth_button_photo_image, command=lambda: on_button_click("./popupcodes/Farm.png"), bd=0, highlightthickness=0)
fourth_button_x = 260  # Adjust the x-coordinate as needed
fourth_button_y = 530  # Adjust the y-coordinate as needed
canvas.create_window(fourth_button_x, fourth_button_y, anchor="center", window=fourth_button)

# Load and resize the fifth button image (duplicate of the second)
fifth_button_image_path = "./popupcodes/Water.png"  # Change this path accordingly
fifth_button_image = Image.open(fifth_button_image_path)
fifth_button_image = fifth_button_image.resize((40, 40))
fifth_button_photo_image = ImageTk.PhotoImage(fifth_button_image)

# Create the fifth button on the canvas with specified coordinates
fifth_button = tk.Button(root, image=fifth_button_photo_image, command=lambda: on_button_click("./popupcodes/WaterPump.png"), bd=0, highlightthickness=0)
fifth_button_x = 520  # Adjust the x-coordinate as needed
fifth_button_y = 410  # Adjust the y-coordinate as needed
canvas.create_window(fifth_button_x, fifth_button_y, anchor="center", window=fifth_button)

# Load and resize the sixth button image (duplicate of the second)
sixth_button_image_path = "./popupcodes/Water.png"  # Change this path accordingly
sixth_button_image = Image.open(sixth_button_image_path)
sixth_button_image = sixth_button_image.resize((40, 40))
sixth_button_photo_image = ImageTk.PhotoImage(sixth_button_image)

# Create the sixth button on the canvas with specified coordinates
sixth_button = tk.Button(root, image=sixth_button_photo_image, command=lambda: on_button_click("./popupcodes/WaterPump.png"), bd=0, highlightthickness=0)
sixth_button_x = 550  # Adjust the x-coordinate as needed
sixth_button_y = 600  # Adjust the y-coordinate as needed
canvas.create_window(sixth_button_x, sixth_button_y, anchor="center", window=sixth_button)

# Start the main loop in a separate thread
loop_thread = threading.Thread(target=update_statuses)
loop_thread.start()

# Start Tkinter main loop
root.mainloop()


#drag and drop x3
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

class DraggableImage:
    def __init__(self, canvas, image_path, initial_x, initial_y, size=(200, 200)):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.image_id = canvas.create_image(initial_x, initial_y, anchor="nw", image=self.photo_image)

        # Bind mouse events for dragging
        canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.on_press)
        canvas.tag_bind(self.image_id, "<B1-Motion>", self.on_drag)

        self.last_x = 0
        self.last_y = 0

    def on_press(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_drag(self, event):
        delta_x = event.x - self.last_x
        delta_y = event.y - self.last_y
        self.canvas.move(self.image_id, delta_x, delta_y)
        self.last_x = event.x
        self.last_y = event.y

def display_background_image(image_paths):
    root = Tk()
    root.title("Draggable Image Example")

    canvas = Canvas(root, width=750, height=750)
    canvas.pack()

    # Create DraggableImage instances for each image
    draggable_image1 = DraggableImage(canvas, image_paths[0], 0, 0)
    draggable_image2 = DraggableImage(canvas, image_paths[1], 100, 100)
    draggable_image3 = DraggableImage(canvas, image_paths[2], 200, 200)

    root.mainloop()

# Provide paths to your image files
image_paths = ["./popupcodes/StrawSeeds.png", "./popupcodes/appleseeds.png", "./popupcodes/orangeseeds.png"]

# Call the function to display the draggable images
display_background_image(image_paths)



