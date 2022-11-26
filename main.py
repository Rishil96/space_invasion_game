# Space Invasion Game
import pygame
import random

# Initialize pygame
pygame.init()

# Display the screen
screen = pygame.display.set_mode(size=(800, 600))

# Title and Icon
pygame.display.set_caption("Space Invasion")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Background image
background = pygame.image.load("images/Background.jpg")

# Create player variables
player_image = pygame.image.load("images/Rocket.png")
player_x = 368
player_y = 500
player_x_change = 0


# Create player function
def player(x, y):
    screen.blit(player_image, (x, y))


# Create enemy
enemy_image = pygame.image.load("images/enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 200)
enemy_x_change = 1
enemy_y_change = 50


# Create enemy function
def enemy(x, y):
    screen.blit(enemy_image, (x, y))


# Create bullet
bullet_image = pygame.image.load("images/bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 1
is_bullet_visible = False


# shoot bullet
def shoot_bullet(x, y):
    global is_bullet_visible
    is_bullet_visible = True
    screen.blit(bullet_image, (x + 16, y + 10))


# Game loop
is_running = True

while is_running:
    # RGB Background
    # screen.fill((205, 144, 228))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if not is_bullet_visible:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

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
        enemy_x_change = 1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -1
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        is_bullet_visible = False
    if is_bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Player call
    player(player_x, player_y)

    # Enemy call
    enemy(enemy_x, enemy_y)

    # Update screen
    pygame.display.update()
