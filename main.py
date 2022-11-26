# Space Invasion Game
import pygame
import random
import math
from pygame import mixer

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

# Score
score = 0
my_font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10


# End of game text
end_font = pygame.font.Font("freesansbold.ttf", 40)


# Final text score
def final_text():
    my_final_font = end_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_final_font, (250, 200))


# show score
def show_score(x, y):
    text = my_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))


# Create player variables
player_image = pygame.image.load("images/Rocket.png")
player_x = 368
player_y = 500
player_x_change = 0


# Create player function
def player(x, y):
    screen.blit(player_image, (x, y))


# Create enemy
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 7

for each_enemy in range(number_of_enemies):
    enemy_image.append(pygame.image.load("images/enemy.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)


# Create enemy function
def enemy(x, y, en):
    screen.blit(enemy_image[en], (x, y))


# Create bullet
bullet_image = pygame.image.load("images/bullet.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 3
is_bullet_visible = False


# shoot bullet
def shoot_bullet(x, y):
    global is_bullet_visible
    is_bullet_visible = True
    screen.blit(bullet_image, (x + 16, y + 10))


# Detect collision
def bullet_collision_with_enemy(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance < 27


# add music
mixer.music.load("sounds/background_music.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

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

                bullet_sound = mixer.Sound("sounds/shot.mp3")
                bullet_sound.play()

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

    # Modify enemy location
    for each_enemy in range(number_of_enemies):
        # end of game
        if enemy_y[each_enemy] > 500:
            for k in range(number_of_enemies):
                enemy_y[k] = 1000
            final_text()
            break
        enemy_x[each_enemy] += enemy_x_change[each_enemy]

        # Keep player inside the screen
        if enemy_x[each_enemy] <= 0:
            enemy_x_change[each_enemy] = 0.5
            enemy_y[each_enemy] += enemy_y_change[each_enemy]
        elif enemy_x[each_enemy] >= 736:
            enemy_x_change[each_enemy] = -0.5
            enemy_y[each_enemy] += enemy_y_change[each_enemy]

        # Collision
        collision = bullet_collision_with_enemy(enemy_x[each_enemy], enemy_y[each_enemy], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound("sounds/punch.mp3")
            collision_sound.play()
            bullet_y = 500
            is_bullet_visible = False
            score += 1
            enemy_x[each_enemy] = random.randint(0, 736)
            enemy_y[each_enemy] = random.randint(50, 200)

        # Enemy call
        enemy(enemy_x[each_enemy], enemy_y[each_enemy], each_enemy)

    # Bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        is_bullet_visible = False
    if is_bullet_visible:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Player call
    player(player_x, player_y)

    # Display score
    show_score(text_x, text_y)

    # Update screen
    pygame.display.update()
