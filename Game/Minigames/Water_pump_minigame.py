import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (23, 23, 23)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)  # Dark blue color
RED = (255, 0, 0)
GREY = (169, 169, 169)  # Solid grey
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fix the crack in the pipes!")

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

# Water bar
water_bar = 100

# List to store crack positions and values
cracks = []

# Variable to track remaining cracks
remaining_cracks = 0

# Flag to check if the "Good Job" screen is displayed
good_job_screen = False
you_lose_screen = False

# Load and shrink crack image
crack_image_original = pygame.image.load("photos\\CRACK-removebg-preview.png")  # Replace with your actual file path
crack_image = pygame.transform.scale(crack_image_original, (int(crack_image_original.get_width() * 0.1), int(crack_image_original.get_height() * 0.1)))

# Load custom cursor image and make it larger
custom_cursor_image_original = pygame.image.load("photos\\adhesive-electrical-tape-cartoon-illustration-vector-removebg-preview.png")  # Replace with your custom cursor image path
custom_cursor_image = pygame.transform.scale(custom_cursor_image_original, (48, 48))  # Adjust the size here

# Set the custom cursor
pygame.mouse.set_visible(False)  # Hide the default cursor


# Function to draw the pipe at the bottom of the window
def draw_pipe():
    pygame.draw.rect(screen, GREY, (50, 490, 700, 40))  # Solid grey

# Function to draw cracks on the pipe
def draw_cracks():
    for crack in cracks:
        x, y = crack[0]
        crack_value = crack[1]
        crack_rect = crack_image.get_rect(center=(x, y))
        screen.blit(crack_image, crack_rect.topleft)

# Function to check if cracks overlap
def overlaps(new_crack, existing_cracks):
    for crack in existing_cracks:
        distance = pygame.math.Vector2(new_crack[0]) - pygame.math.Vector2(crack[0])
        if distance.length() < 14:  # Adjusted collision check for larger cracks
            return True
    return False

# Function to generate random cracks within the rectangle without overlapping
def generate_cracks():
    global remaining_cracks
    cracks.clear()
    total_value = water_bar
    while total_value != 0:
        value = random.randint(1, min(total_value, 20))
        x = random.randint(60, 740)
        y = random.randint(490, 520)
        new_crack = ((x, y), value, 3)  # Added crack values and clicks_left
        if not overlaps(new_crack, cracks):
            cracks.append(new_crack)
            total_value -= value
    remaining_cracks = len(cracks)

# Function to display "Good Job" screen
def good_job_screen_display():
    screen.fill(LIGHT_BLUE)
    text = big_font.render("Good Job!", True, DARK_BLUE)  # Adjusted text color
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Button rectangle
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, RED, button_rect)
    
    # Button text
    button_text = font.render("Exit", True, WHITE)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    return button_rect  # Return the button rectangle for click detection

# Function to display "You Lose" screen
def you_lose_screen_display():
    screen.fill(LIGHT_BLUE)
    text = big_font.render("You Lose!", True, DARK_BLUE)  # Adjusted text color
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Button rectangle
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, RED, button_rect)
    
    # Button text
    button_text = font.render("Exit", True, WHITE)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    return button_rect  # Return the button rectangle for click detection

# Main game loop
running = True
clock = pygame.time.Clock()

generate_cracks()

# Set the start time for the timer
start_time = pygame.time.get_ticks()

# Time limit in seconds
time_limit = 50

# Variables for win/lose screens
good_job_screen = False
you_lose_screen = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if good_job_screen:
                button_rect = good_job_screen_display()
                if button_rect.collidepoint(event.pos):
                    running = False  # Exit the game when the button is clicked
            elif you_lose_screen:
                button_rect = you_lose_screen_display()
                if button_rect.collidepoint(event.pos):
                    running = False  # Exit the game when the button is clicked
            else:
                # Center the hitbox on the crack image
                clicked_cracks = [crack for crack in cracks if pygame.Rect(crack[0][0] - crack_image.get_width() // 2, crack[0][1] - crack_image.get_height() // 2, crack_image.get_width(), crack_image.get_height()).collidepoint(event.pos)]
                for crack in clicked_cracks:
                    x, y = crack[0]
                    crack_value, clicks_left = crack[1], crack[2]
                    if clicks_left > 0:
                        water_bar -= crack_value
                        clicks_left -= 1
                        if clicks_left == 0:
                            remaining_cracks -= 1
                            if remaining_cracks == 0:
                                good_job_screen = True
                    cracks.remove(crack)
                    if clicks_left > 0:  # Append only if clicks_left is still greater than 0
                        cracks.append(((x, y), crack_value, clicks_left))

    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = max(0, time_limit - elapsed_time)

    if time_left == 0 and not good_job_screen:
        you_lose_screen = True

    screen.fill(LIGHT_BLUE)

    draw_pipe()  # Moved the drawing of the pipe to show outline
    draw_cracks()

    if good_job_screen:
        button_rect = good_job_screen_display()
    elif you_lose_screen:
        button_rect = you_lose_screen_display()
    else:
        # Display time left
        time_text = font.render(f"Time Left: {time_left} seconds", True, WHITE)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 20, 20))
        # Display remaining cracks
        cracks_left_text = font.render(f"Cracks Left: {remaining_cracks}", True, WHITE)
        screen.blit(cracks_left_text, (20, 20))

    # Update the custom cursor position
    screen.blit(custom_cursor_image, pygame.mouse.get_pos())

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
