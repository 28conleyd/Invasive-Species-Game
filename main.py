import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invasive Species Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 5

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    pygame.display.flip()

pygame.quit()
sys.exit()
