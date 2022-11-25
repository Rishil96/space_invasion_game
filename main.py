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

# Create player
player_image = pygame.image.load("Rocket.png")
player_x = 368
player_y = 536


def player():
    screen.blit(player_image, (player_x, player_y))


# Game loop
is_running = True

while is_running:
    # RGB Background
    screen.fill((205, 144, 228))

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            is_running = False

    player()

    pygame.display.update()
