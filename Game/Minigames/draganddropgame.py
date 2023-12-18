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
home_colors = [generate_random_color() for _ in range(3)]
for i, color in enumerate(home_colors):
    w = 30
    h = 30
    x = SCREEN_WIDTH // 2 - (len(home_colors) * w + (len(home_colors) - 1) * 80) // 2 + i * (w + 80)
    y = SCREEN_HEIGHT - 50  # Centered at the bottom
    home_rect = pygame.Rect(x, y, w, h)
    homes.append((home_rect, color))

# Create colored boxes with matching home colors
for i in range(3):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = 50
    h = 50
    home_color = home_colors[i]
    box_rect = pygame.Rect(x, y, w, h)
    box_color = home_color  # Use home color as the box color
    boxes.append((box_rect, box_color))

# You win screen
font = pygame.font.Font(None, 36)
you_win_text = font.render("You Win!", True, (0, 0, 0))  # Change color to black
you_win_rect = you_win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Overlay images for each box
overlay_images = [pygame.image.load('photos\\appleseeds.sprite.png').convert_alpha(),
                  pygame.image.load('photos\\orangeseeds.sprite.png').convert_alpha(),
                  pygame.image.load('photos\\strawberryseeds.sprite.png').convert_alpha()]

# Scale overlay images to match box size
overlay_images = [pygame.transform.scale(img, (100, 100)) for img in overlay_images]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, (box_rect, _) in enumerate(boxes):
                    if box_rect.collidepoint(event.pos):
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
                for home_rect, home_color in homes:
                    if home_rect.colliderect(boxes[active_box][0]):
                        if home_color == boxes[active_box][1]:
                            # Box is in the correct home
                            active_box = None
                            break

    # Draw background
    screen.fill("white")

    # Draw homes
    for home_rect, color in homes:
        pygame.draw.rect(screen, color, home_rect)

    # Draw colored boxes
    for box_rect, box_color in boxes:
        pygame.draw.rect(screen, box_color, box_rect)

    # Draw overlay images on top of boxes
    for (box_rect, _), overlay_image in zip(boxes, overlay_images):
        overlay_rect = box_rect.copy()  # Create a copy of the box rect for the overlay
        screen.blit(overlay_image, overlay_rect.topleft)

    # Check if all boxes are in their correct homes (win condition)
    if all(home_rect.colliderect(box_rect) and home_color == box_color for (box_rect, box_color), (home_rect, home_color) in zip(boxes, homes)):
        screen.blit(you_win_text, you_win_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
