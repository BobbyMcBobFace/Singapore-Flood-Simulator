import tkinter as tk
import pygame
import sys
import threading

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600

# Tkinter root window
root = tk.Tk()
root.title("Water and Food Status")

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
    canvas.create_rectangle((width - bar_width) // 15, 50, (width - bar_width) // 15 + bar_fill_width, 50 + bar_height, fill=green)

    # Display the water status label
    water_label.config(text="Water: {}/{}".format(water_current, water_max))

# Function to draw the food status bar and label
def draw_food_status():
    # Draw the food stat bar at the top
    bar_fill_width = int(bar_width * (food_current / food_max))
    canvas.create_rectangle((width - bar_width) // 15, 150, (width - bar_width) // 15 + bar_fill_width, 150 + bar_height, fill=blue)

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

# Create a canvas for drawing
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Display the water and food status labels
water_label = tk.Label(root, text="Water: {}/{}".format(water_current, water_max), font=font)
water_label.place(x=10, y=10)

food_label = tk.Label(root, text="Food: {}/{}".format(food_current, food_max), font=font)
food_label.place(x=10, y=40)

# Start the main loop in a separate thread
loop_thread = threading.Thread(target=update_statuses)
loop_thread.start()

# Start Tkinter main loop
root.mainloop()
