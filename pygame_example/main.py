import pygame, sys
from pygame import Vector2
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

playerX = 800
playerY = 450
velocity = Vector2(0, 0)

# The main function that controls the game

looping = True

# The main game loop
while looping:
    # Get inputs
    keysPressed = pygame.key.get_pressed()

    movement_vector = Vector2(0, 0)

    if keysPressed[pygame.K_LEFT]:
        movement_vector.x += -1

    if keysPressed[pygame.K_RIGHT]:
        movement_vector.x += 1

    if keysPressed[pygame.K_UP]:
        movement_vector.y += -1

    if keysPressed[pygame.K_DOWN]:
        movement_vector.y += 1

    movement_vector = Vector2(0, 0) if movement_vector.magnitude_squared() == 0 else movement_vector.normalize()

    velocity.x += movement_vector.x
    velocity.y += movement_vector.y

    playerX += velocity.x
    playerY += velocity.y

    velocity.x *= 0.96
    velocity.y *= 0.96

    if keysPressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Processing
    # This section will be built out later

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.draw.circle(WINDOW, (255, 0, 0), (playerX, playerY), 20)

    pygame.display.update()
    fpsClock.tick(FPS)
