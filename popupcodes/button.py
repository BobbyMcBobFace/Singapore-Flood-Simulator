#StrawSeeds draggable
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

class DraggableImage:
    def __init__(self, canvas, image_path, initial_x, initial_y):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize((200, 200))
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

def display_background_image(image_path):
    root = Tk()
    root.title("Draggable Image Example")

    canvas = Canvas(root, width=750, height=750)
    canvas.pack()

    # Create a DraggableImage instance
    draggable_image = DraggableImage(canvas, image_path, 0, 0)

    root.mainloop()

display_background_image("./popupcodes/StrawSeeds.png")


#appleseeds
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def display_background_image(image_path):
    root = Tk()
    root.title("Background Image Example")
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(image)
    canvas = Canvas(root, width=750, height=750)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo_image)
    root.mainloop()
display_background_image("./popupcodes/appleseeds.png")

#orangeseeds
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def display_background_image(image_path):
    root = Tk()
    root.title("Background Image Example")
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(image)
    canvas = Canvas(root, width=750, height=750)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo_image)
    root.mainloop()
display_background_image("./popupcodes/orangeseeds.png")

#applepot
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def display_background_image(image_path):
    root = Tk()
    root.title("Background Image Example")
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(image)
    canvas = Canvas(root, width=750, height=750)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo_image)
    root.mainloop()
display_background_image("./popupcodes/strawseeds.png")


#orangepot
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def display_background_image(image_path):
    root = Tk()
    root.title("Background Image Example")
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(image)
    canvas = Canvas(root, width=750, height=750)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo_image)
    root.mainloop()
display_background_image("./popupcodes/orangepot.png")


#strawpot
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

def display_background_image(image_path):
    root = Tk()
    root.title("Background Image Example")
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo_image = ImageTk.PhotoImage(image)
    canvas = Canvas(root, width=750, height=750)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=photo_image)
    root.mainloop()
display_background_image("./popupcodes/strawpot.png")



#3 pots
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk

class StaticImage:
    def __init__(self, canvas, image_path, initial_x, initial_y, size=(200, 200)):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.image_id = canvas.create_image(initial_x, initial_y, anchor="nw", image=self.photo_image)

def display_static_images(image_paths):
    root = Tk()
    root.title("Multiple Static Images Example")

    canvas = Canvas(root, width=750, height=750)
    canvas.pack()

    # Create StaticImage instances for each image
    static_image1 = StaticImage(canvas, image_paths[0], 150, 500)
    static_image2 = StaticImage(canvas, image_paths[1], 300, 500)
    static_image3 = StaticImage(canvas, image_paths[2], 450, 500)

    root.mainloop()

# Provide paths to your image files
image_paths = ["./popupcodes/strawpot.png", "./popupcodes/applepot.png", "./popupcodes/orangepot.png"]

# Call the function to display the static images (non-draggable)
display_static_images(image_paths)




#ragggy
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


#fdgergerh
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
    def __init__(self, canvas, image_path, initial_x, initial_y, target_x, target_y, size=(200, 200)):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.image_id = canvas.create_image(initial_x, initial_y, anchor="nw", image=self.photo_image)

        self.target_x = target_x
        self.target_y = target_y

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

        # Check if the seed is within the boundaries of its allocated pot
        seed_bbox = self.canvas.bbox(self.image_id)
        pot_bbox = self.canvas.bbox(self.target_x)
        if self.is_inside(seed_bbox, pot_bbox):
            # Seed is inside the pot, update the score
            update_score()

    @staticmethod
    def is_inside(bbox1, bbox2):
        # Check if bbox1 is inside bbox2
        x1, y1, x2, y2 = bbox1
        return x2 <= bbox2[2] and y2 <= bbox2[3] and x1 >= bbox2[0] and y1 >= bbox2[1]

def update_score():
    global score
    score += 1
    canvas.itemconfig(score_label, text=f"Score: {score}")

def display_combined_images(static_image_paths, draggable_image_paths):
    global score
    score = 0

    root = Tk()
    root.title("Combined Image Example")

    canvas = Canvas(root, width=900, height=750)
    canvas.pack()

    # Create StaticImage instances for each image
    static_image1 = StaticImage(canvas, static_image_paths[0], 150, 500)
    static_image2 = StaticImage(canvas, static_image_paths[1], 300, 500)
    static_image3 = StaticImage(canvas, static_image_paths[2], 450, 500)

    # Create DraggableImage instances for each image
    draggable_image1 = DraggableImage(canvas, draggable_image_paths[0], 300, 100, 450, 500)
    draggable_image2 = DraggableImage(canvas, draggable_image_paths[1], 450, 100, 150, 500)
    draggable_image3 = DraggableImage(canvas, draggable_image_paths[2], 150, 100, 300, 500)

    score_label = canvas.create_text(50, 50, text="Score: 0", anchor="nw", font=("Arial", 16), fill="black")

    root.mainloop()

# Provide paths to your image files
static_image_paths = ["./popupcodes/strawpot.png", "./popupcodes/applepot.png", "./popupcodes/orangepot.png"]
draggable_image_paths = ["./popupcodes/StrawSeeds.png", "./popupcodes/appleseeds.png", "./popupcodes/orangeseeds.png"]

# Call the function to display both static and draggable images on one screen
display_combined_images(static_image_paths, draggable_image_paths)


#more saves
from tkinter import Tk, Canvas, Label, PhotoImage
from PIL import Image, ImageTk

def on_hitbox_click(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def on_drag(event):
    global last_x, last_y
    canvas.move(hitbox1, event.x - last_x, event.y - last_y)
    last_x, last_y = event.x, event.y
    check_collision()

def check_collision():
    global score
    hitbox_bbox = canvas.bbox(hitbox1)
    overlapping_items = canvas.find_overlapping(*hitbox_bbox)

    for item in overlapping_items:
        if item != hitbox1:
            print("Collision with", item)
            if score == 0:  # Check if the image has not scored before
                update_score()

def update_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

root = Tk()
root.title("First Image Example")

# Initialize the canvas widget
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

# Load and resize the first background image
first_image_path = "./popupcodes/strawseeds.png"
first_image = Image.open(first_image_path)
first_image = first_image.resize((200, 200))
first_photo_image = ImageTk.PhotoImage(first_image)

# Create the first hitbox using the first background image
hitbox1 = canvas.create_image(100, 100, anchor="nw", image=first_photo_image)
canvas.tag_bind(hitbox1, "<Button-1>", on_hitbox_click)

# Make the hitbox draggable
last_x, last_y = 0, 0
score = 0

# Create a label for the scoreboard
score_label = Label(root, text=f"Score: {score}", font=("Arial", 16), bg="white")
score_label_id = canvas.create_window(10, 10, anchor="nw", window=score_label)

canvas.tag_bind(hitbox1, "<ButtonPress-1>", lambda event: on_hitbox_click(event))
canvas.tag_bind(hitbox1, "<B1-Motion>", lambda event: on_drag(event))

root.mainloop()



from tkinter import Tk, Canvas, Label, PhotoImage
from PIL import Image, ImageTk

def on_hitbox_click(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def on_drag(event, hitbox):
    global last_x, last_y
    canvas.move(hitbox, event.x - last_x, event.y - last_y)
    last_x, last_y = event.x, event.y
    check_collision(hitbox)

def check_collision(hitbox):
    global score
    hitbox_bbox = canvas.bbox(hitbox)
    overlapping_items = canvas.find_overlapping(*hitbox_bbox)

    for item in overlapping_items:
        if item != hitbox:
            print("Collision with", item)
            if score == 0:  # Check if the image has not scored before
                update_score()

def update_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

root = Tk()
root.title("Combined Example")

# Initialize the canvas widget
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

# Load and resize the first background image
first_image_path = "./popupcodes/applepot.png"
first_image = Image.open(first_image_path)
first_image = first_image.resize((200, 200))
first_photo_image = ImageTk.PhotoImage(first_image)

# Create the first hitbox using the first background image
hitbox1 = canvas.create_image(100, 100, anchor="nw", image=first_photo_image)
canvas.tag_bind(hitbox1, "<Button-1>", lambda event: on_hitbox_click(event))
canvas.tag_bind(hitbox1, "<B1-Motion>", lambda event: on_drag(event, hitbox1))

# Load and resize the second image
second_image_path = "./popupcodes/appleseeds.png"
second_image = Image.open(second_image_path)
second_image = second_image.resize((200, 200))
second_photo_image = ImageTk.PhotoImage(second_image)

# Create another hitbox using the second image
hitbox2 = canvas.create_image(600, 600, anchor="nw", image=second_photo_image)
canvas.tag_bind(hitbox2, "<Button-1>", lambda event: on_hitbox_click(event))
canvas.tag_bind(hitbox2, "<B1-Motion>", lambda event: on_drag(event, hitbox2))

# Load and resize the third image
third_image_path = "./popupcodes/strawseeds.png"
third_image = Image.open(third_image_path)
third_image = third_image.resize((200, 200))
third_photo_image = ImageTk.PhotoImage(third_image)

# Create another hitbox using the third image
hitbox3 = canvas.create_image(300, 300, anchor="nw", image=third_photo_image)
canvas.tag_bind(hitbox3, "<Button-1>", lambda event: on_hitbox_click(event))
canvas.tag_bind(hitbox3, "<B1-Motion>", lambda event: on_drag(event, hitbox3))

# Make the hitboxes draggable
last_x, last_y = 0, 0
score = 0

# Create a label for the scoreboard
score_label = Label(root, text=f"Score: {score}", font=("Arial", 16), bg="white")
score_label_id = canvas.create_window(10, 10, anchor="nw", window=score_label)

root.mainloop()

