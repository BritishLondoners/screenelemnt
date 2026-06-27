import pygame
import sys

# Initialize Pygame
pygame.init()

# Window size
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

# Colors
WHITE = (255, 255, 255)
RECT_COLOR = (0, 128, 255)  # You can change this to any color

# Font setup
font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, (0, 0, 0))  # Black text

# Rectangle setup (centered)
rect_width, rect_height = 200, 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, RECT_COLOR, rectangle)

    # Draw text
    screen.blit(text, (200, 50))  # Position text near the top

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
