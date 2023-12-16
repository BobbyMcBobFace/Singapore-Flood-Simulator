import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stats Bar at the Top Example")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (152,245,255)
blue =  (69,139,0)

# Note to the autistic black yellow, set player water value to water_current and player food value to food_current

water_current = 69
water_max = 100

food_current = 69
food_max = 100

# Set up the stat bar dimensions
bar_width = 400
bar_height = 20

# Set up the font
font = pygame.font.Font(None, 36)

def draw_stat_bar(x, y, current_stat, max_stat, color, label):
    # Calculate the width of the bar based on the current_stat and max_stat
    bar_fill_width = int(bar_width * (current_stat / max_stat))

    # Draw the background bar
    pygame.draw.rect(screen, white, (x, y, bar_width, bar_height))

    # Draw the filled part of the bar
    pygame.draw.rect(screen, color, (x, y, bar_fill_width, bar_height))

    # Display the current_stat value
    text = font.render(f"{label}: {current_stat}/{max_stat}", True, black)
    screen.blit(text, (x + 10, y - 30))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the current_stat values (replace this with your own logic)


    # Clear the screen
    screen.fill(white)

    # Draw the water stat bar at the top
    draw_stat_bar((width - bar_width) // 15, 50, water_current, water_max, green, "Water")

    # Draw the food stat bar at the top
    draw_stat_bar((width - bar_width) // 15, 150, food_current, food_max, blue, "Food")

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
