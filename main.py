# Space Invasion Game
import pygame
import random

# Initialize pygame
pygame.init()

# Display the screen
screen = pygame.display.set_mode(size=(800, 600))

# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Create player variables
player_image = pygame.image.load("Rocket.png")
player_x = 368
player_y = 500
player_x_change = 0


# Create player function
def player(x, y):
    screen.blit(player_image, (x, y))


# Create enemy
enemy_image = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 0.3
enemy_y_change = 50


# Create enemy function
def enemy(x, y):
    screen.blit(enemy_image, (x, y))


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

    # Modify player location
    player_x += player_x_change

    # Keep player inside the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Modify player location
    enemy_x += enemy_x_change

    # Keep player inside the screen
    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change

    # Player call
    player(player_x, player_y)

    # Enemy call
    enemy(enemy_x, enemy_y)

    # Update screen
    pygame.display.update()
