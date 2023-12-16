import pygame
import sys
pygame.init()

width = 700
height = 550

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Window")

clock = pygame.time.Clock()  # Create a clock object to control the frame rate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game logic here

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill the screen with a white color

    # Draw game elements here

    pygame.display.update()

    clock.tick(60)  # Cap the frame rate to 60 frames per second




