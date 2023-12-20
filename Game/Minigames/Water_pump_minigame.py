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

# Function to draw the water bar
def draw_water_bar():
    pygame.draw.rect(screen, DARK_BLUE, (50, 50, water_bar * 5, 40))  # Changed color to dark blue
    pygame.draw.rect(screen, RED, (50, 50, 500, 40), 2)
    text = font.render("Water Being Lost", True, WHITE)  # Changed text inside the bar
    text_rect = text.get_rect(center=(300, 70))  # Adjusted text position
    screen.blit(text, text_rect)

# Function to draw the pipe at the bottom of the window
def draw_pipe():
    pygame.draw.rect(screen, GREY, (50, 500, 700, 40))  # Solid grey

# Function to draw cracks on the pipe
def draw_cracks():
    for crack in cracks:
        pygame.draw.circle(screen, BLACK, crack[0], 7)  # Changed color to dark blue

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
        new_crack = ((x, y), value)  # Added crack values
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

# Main game loop
running = True
clock = pygame.time.Clock()

generate_cracks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if good_job_screen:
                button_rect = good_job_screen_display()
                if button_rect.collidepoint(event.pos):
                    running = False  # Exit the game when the button is clicked
            else:
                clicked_cracks = [crack for crack in cracks if pygame.Rect(crack[0][0] - 7, crack[0][1] - 7, 14, 14).collidepoint(event.pos)]
                for crack in clicked_cracks:
                    water_bar -= crack[1]
                    remaining_cracks -= 1
                    cracks.remove(crack)
                    if remaining_cracks == 0:
                        good_job_screen = True

    screen.fill(LIGHT_BLUE)

    draw_pipe()  # Moved the drawing of the pipe to show outline
    draw_cracks()

    draw_water_bar()  # Draw water bar after other elements to appear above them

    if good_job_screen:
        button_rect = good_job_screen_display()

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()