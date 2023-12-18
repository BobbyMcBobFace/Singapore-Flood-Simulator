import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Farming Game')

active_box = None
boxes = []
homes = []

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Create homes
home_colors = [generate_random_color() for _ in range(5)]
for i, color in enumerate(home_colors):
    x = 20
    y = 20 + i * 80
    w = 30
    h = 30
    home = pygame.Rect(x, y, w, h)
    homes.append((home, color))

# Create colored boxes with matching home colors
for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = 50
    h = 50
    home_color = home_colors[i]
    box = pygame.Rect(x, y, w, h)
    boxes.append((box, home_color))

# You win screen
font = pygame.font.Font(None, 36)
you_win_text = font.render("You Win!", True, (0, 0, 0))  # Change color to black
you_win_rect = you_win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

run = True
while run:
    screen.fill("white")

    # Draw homes
    for home, color in homes:
        pygame.draw.rect(screen, color, home)

    # Draw boxes
    for box, box_color in boxes:
        pygame.draw.rect(screen, box_color, box)

    # Check if all boxes are in their correct homes (win condition)
    if all(home.colliderect(box) and home_color == box_color for (box, box_color), (home, home_color) in zip(boxes, homes)):
        screen.blit(you_win_text, you_win_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Display "You Win!" for 2 seconds
        run = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, (box, _) in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box is not None:
                # Move the box
                boxes[active_box][0].move_ip(event.rel)

                # Check if the box is out of bounds
                if boxes[active_box][0].left < 0:
                    boxes[active_box][0].left = 0
                elif boxes[active_box][0].right > SCREEN_WIDTH:
                    boxes[active_box][0].right = SCREEN_WIDTH

                if boxes[active_box][0].top < 0:
                    boxes[active_box][0].top = 0
                elif boxes[active_box][0].bottom > SCREEN_HEIGHT:
                    boxes[active_box][0].bottom = SCREEN_HEIGHT

                # Check if the box is inside its home
                for home, home_color in homes:
                    if home.colliderect(boxes[active_box][0]):
                        if home_color == boxes[active_box][1]:
                            # Box is in the correct home
                            active_box = None
                            break

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
sys.exit()
