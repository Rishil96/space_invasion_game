# Space Invasion Game
import pygame

# Initialize pygame
pygame.init()

# Display the screen
screen = pygame.display.set_mode(size=(800, 600))

# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Game loop
is_running = True

while is_running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            is_running = False
    screen.fill((205, 144, 228))
    pygame.display.update()
