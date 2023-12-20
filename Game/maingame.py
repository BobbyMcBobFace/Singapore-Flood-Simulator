import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import subprocess
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1920, 1080

# Tkinter root window
root = tk.Tk()
root.title("Game Interface")

# Set the window to full screen
root.attributes('-fullscreen', True)

# Set up colors
green = "#98F5FF"
blue = "#458B00"

# Set up the stat bar dimensions
bar_width = 400
bar_height = 20

# Set up the font
font = ("Arial", 16)

# Initial water status
water_current = 50
water_max = 100

food_current = 50
food_max = 100

# Function to draw the water status bar and label
def draw_water_status():
    # Draw the water stat bar at the bottom
    bar_fill_width = int(bar_width * (water_current / water_max))
    shift_amount = 20  # Adjust the amount you want to shift
    start_x = (width - bar_width) // 2 - shift_amount
    end_x = start_x + bar_fill_width
    canvas.create_rectangle(start_x, 50, end_x, 50 + bar_height, fill=green)

    # Display the water status label
    water_label.config(text="Water: {}/{}".format(water_current, water_max))

    # Schedule the function to run again after 100 milliseconds
    root.after(100, draw_water_status)

# Function to draw the food status bar and label
def draw_food_status():
    # Draw the food stat bar at the bottom
    bar_fill_width = int(bar_width * (food_current / food_max))
    shift_amount = 20  # Adjust the amount you want to shift
    start_x = (width - bar_width) // 2 - shift_amount
    end_x = start_x + bar_fill_width
    canvas.create_rectangle(start_x, 90, end_x, 90 + bar_height, fill=blue)

    # Display the food status label
    food_label.config(text="Food: {}/{}".format(food_current, food_max))

    # Schedule the function to run again after 100 milliseconds
    root.after(100, draw_food_status)




# Main game loop
def update_statuses():
    # Initial call to start the loop
    draw_water_status()
    draw_food_status()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

    # Schedule the function to run again after 100 milliseconds
    root.after(100, update_statuses)

# Function to handle button click s
def on_button_click(minigame_type):
    new_window = tk.Toplevel(root)

    # Run the external Python program when a button is clicked
    if minigame_type == "food":
        result = run_food_minigame()
        update_food(result)
    elif minigame_type == "water":
        result = run_water_minigame()
        update_water(result)

def run_food_minigame():
    # Open the food minigame script and wait for it to finish
    subprocess.call(["python", "Game\\Minigames\\farmSortingGame.py"])

    return 5

def run_water_minigame():
    # Open the water minigame script and wait for it to finish
    subprocess.call(["python", "Game\\Minigames\\Water_pump_minigame.py"])

    return 7

def update_food(amount):
    # Update the food level in the main game
    global food_current
    food_current += amount
    if food_current > food_max:
        food_current = food_max

    # Update the food status bar and label
    draw_food_status()

def update_water(amount):
    # Update the water level in the main game
    global water_current
    water_current += amount
    if water_current > water_max:
        water_current = water_max

    # Update the water status bar and label
    draw_water_status()

# Create a canvas for drawing
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()


# Load and resize the map image
map_image_path = "photos\\Untitled.png"
map_image = Image.open(map_image_path)
map_image = map_image.resize((1550, 850))
map_photo_image = ImageTk.PhotoImage(map_image)

# Create a canvas for the map image
canvas.create_image(0, 0, anchor="nw", image=map_photo_image)

# Load and resize the ship image
ship_image_path = "./popupcodes/Ship.png"
ship_image = Image.open(ship_image_path)
ship_image = ship_image.resize((150, 150))
ship_photo_image = ImageTk.PhotoImage(ship_image)

# Create a canvas for the ship image
ship_canvas = canvas.create_image(930, 650, anchor="center", image=ship_photo_image)
# Create a canvas for the ship image
ship1_canvas = canvas.create_image(1030, 650, anchor="center", image=ship_photo_image)

# Load and resize the second aesthetic picture (Cargo.png)
cargo_image_path = "./popupcodes/Cargo.png"
cargo_image = Image.open(cargo_image_path)
cargo_image = cargo_image.resize((140, 140))
cargo_photo_image = ImageTk.PhotoImage(cargo_image)

# Create a canvas for the second aesthetic picture
cargo_canvas = canvas.create_image(250, 670, anchor="center", image=cargo_photo_image)

cargo1_canvas = canvas.create_image(550, 600, anchor="center", image=cargo_photo_image)

cargo2_canvas = canvas.create_image(60  0, 70, anchor="center", image=cargo_photo_image)
# Load and resize the third aesthetic picture (Airport.png)
airport_image_path = "./popupcodes/Airport.png"
airport_image = Image.open(airport_image_path)
airport_image = airport_image.resize((250, 250))
airport_photo_image = ImageTk.PhotoImage(airport_image)

# Create a canvas for the third aesthetic picture
airport_canvas = canvas.create_image(1260, 400, anchor="center", image=airport_photo_image)

airport1_image_path = "./popupcodes/Airport.png"
airport1_image = Image.open(airport_image_path)
airport1_image = airport_image.resize((90, 90))
airport1_photo_image = ImageTk.PhotoImage(airport1_image)

# Create a canvas for the third aesthetic picture
airport1_canvas = canvas.create_image(430, 800, anchor="center", image=airport1_photo_image)

airport2_image_path = "./popupcodes/Airport.png"
airport2_image = Image.open(airport_image_path)
airport2_image = airport_image.resize((150, 150))
airport2_photo_image = ImageTk.PhotoImage(airport2_image)

# Create a canvas for the third aesthetic picture
airport2_canvas = canvas.create_image(863, 200, anchor="center", image=airport2_photo_image)

# Display the water and food status labels
water_label = tk.Label(root, text="Water: {}/{}".format(water_current, water_max), font=font)
water_label.place(x=10, y=10)

food_label = tk.Label(root, text="Food: {}/{}".format(food_current, food_max), font=font)
food_label.place(x=10, y=40)


# Counter and timestamp variables for tracking Escape key presses
escape_press_count = 0
last_escape_press_time = 0

# Function to handle Escape key presses
def on_escape_press(event):
    global escape_press_count, last_escape_press_time

    current_time = time.time()

    # Check if the last Escape press was within a short time frame
    if current_time - last_escape_press_time < 1:
        escape_press_count += 1
    else:
        escape_press_count = 1  # Reset the count if it's been too long

    last_escape_press_time = current_time

    # Check if Escape key is pressed three times in quick succession
    if escape_press_count == 3:
        # Ask the user if they want to close the program
        result = messagebox.askquestion("Exit", "Do you want to close the program?")
        if result == "yes":
            root.destroy()  # Close the Tkinter window

# Bind the Escape key to the callback function
root.bind('<Escape>', on_escape_press)


# Load and resize the first button image
first_button_image_path = "photos\\farm.sprite.PNG"  # Change this path accordingly
first_button_image = Image.open(first_button_image_path).convert("RGBA")
first_button_image = first_button_image.resize((60, 60))
first_button_photo_image = ImageTk.PhotoImage(first_button_image)


# Create the first button on the canvas with specified coordinates
first_button = tk.Button(root, image=first_button_photo_image, command=lambda: on_button_click( "food"), bd=0, highlightthickness=0)
first_button_x = 390  
first_button_y = 190
canvas.create_window(first_button_x, first_button_y, anchor="center", window=first_button)

# Load and resize the second button image
second_button_image_path = "photos\\farm.sprite.PNG"
second_button_image = Image.open(second_button_image_path)
second_button_image = second_button_image.resize((60, 60))
second_button_photo_image = ImageTk.PhotoImage(second_button_image)

# Create the second button on the canvas with specified coordinates
second_button = tk.Button(root, image=second_button_photo_image, command=lambda: on_button_click("food"), bd=0, highlightthickness=0)
second_button_x = 800
second_button_y = 290
canvas.create_window(second_button_x, second_button_y, anchor="center", window=second_button)

# Load and resize the third button image
third_button_image_path = "photos\\farm.sprite.PNG"  # Change this path accordingly
third_button_image = Image.open(third_button_image_path)
third_button_image = third_button_image.resize((60, 60))
third_button_photo_image = ImageTk.PhotoImage(third_button_image)

# Create the third button on the canvas with specified coordinates
third_button = tk.Button(root, image=third_button_photo_image, command=lambda: on_button_click("food"), bd=0, highlightthickness=0)
third_button_x = 330  # Adjust the x-coordinate as needed
third_button_y = 290  # Adjust the y-coordinate as needed
canvas.create_window(third_button_x, third_button_y, anchor="center", window=third_button)

# Load and resize the fourth button image (duplicate of the first and third)
fourth_button_image_path = "photos\\waterdam.sprite.png"  # Change this path accordingly
fourth_button_image = Image.open(fourth_button_image_path)
fourth_button_image = fourth_button_image.resize((60, 60))
fourth_button_photo_image = ImageTk.PhotoImage(fourth_button_image)

# Create the fourth button on the canvas with specified coordinates
fourth_button = tk.Button(root, image=fourth_button_photo_image, command=lambda: on_button_click("water"), bd=0, highlightthickness=0)
fourth_button_x = 1450  # Adjust the x-coordinate as needed
fourth_button_y = 240  # Adjust the y-coordinate as needed
canvas.create_window(fourth_button_x, fourth_button_y, anchor="center", window=fourth_button)

# Load and resize the fifth button image (duplicate of the second)
fifth_button_image_path = "photos\\waterdam.sprite.png"  # Change this path accordingly
fifth_button_image = Image.open(fifth_button_image_path)
fifth_button_image = fifth_button_image.resize((60, 60))
fifth_button_photo_image = ImageTk.PhotoImage(fifth_button_image)

# Create the fifth button on the canvas with specified coordinates
fifth_button = tk.Button(root, image=fifth_button_photo_image, command=lambda: on_button_click("water"), bd=0, highlightthickness=0)
fifth_button_x = 520  # Adjust the x-coordinate as needed
fifth_button_y = 500  # Adjust the y-coordinate as needed
canvas.create_window(fifth_button_x, fifth_button_y, anchor="center", window=fifth_button)

# Load and resize the sixth button image (duplicate of the second)
sixth_button_image_path = "photos\\waterdam.sprite.png"  # Change this path accordingly
sixth_button_image = Image.open(sixth_button_image_path)
sixth_button_image = sixth_button_image.resize((60, 60))
sixth_button_photo_image = ImageTk.PhotoImage(sixth_button_image)

# Create the sixth button on the canvas with specified coordinates
sixth_button = tk.Button(root, image=sixth_button_photo_image, command=lambda: on_button_click( "water"), bd=0, highlightthickness=0)
sixth_button_x = 1100  # Adjust the x-coordinate as needed
sixth_button_y = 400  # Adjust the y-coordinate as needed
canvas.create_window(sixth_button_x, sixth_button_y, anchor="center", window=sixth_button)

# Start Tkinter main loop
root.mainloop()
