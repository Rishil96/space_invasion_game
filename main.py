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
player_x_change = 0


def player(x, y):
    screen.blit(player_image, (x, y))


# Game loop
is_running = True

while is_running:
    # RGB Background
    screen.fill((205, 144, 228))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Modify location
    player_x += player_x_change

    # Keep inside the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Player call
    player(player_x, player_y)

    # Update screen
    pygame.display.update()
