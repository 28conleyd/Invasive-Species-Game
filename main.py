import os
import sys
import random

# Headless mode for Codespaces
if "CODESPACES" in os.environ:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invasive Species Defender")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 48)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(400, 300, 40, 40)
speed = 5

# Game state
score = 0
lives = 3
game_over = False
win = False
message = ""
message_timer = 0

# Species data
species_list = [
    {"name": "Zebra Mussel", "type": "invasive"},
    {"name": "Kudzu", "type": "invasive"},
    {"name": "Asian Carp", "type": "invasive"},
    {"name": "Oak Tree", "type": "native"},
    {"name": "Monarch Butterfly", "type": "native"},
]

def spawn_species():
    s = random.choice(species_list)
    rect = pygame.Rect(
        random.randint(50, WIDTH - 50),
        random.randint(50, HEIGHT - 50),
        30,
        30
    )
    return {"rect": rect, "data": s}

species = spawn_species()

# Draw text helper
def draw_text(text, x, y, color=BLACK, big=False):
    t = big_font.render(text, True, color) if big else font.render(text, True, color)
    screen.blit(t, (x, y))

# Game loop
running = True
print("Game started successfully")

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                if player.colliderect(species["rect"]):
                    if species["data"]["type"] == "invasive":
                        score += 1
                        message = f"Correct! {species['data']['name']} is invasive."
                    else:
                        lives -= 1
                        message = f"Oops! {species['data']['name']} is native."
                    message_timer = 120
                    species = spawn_species()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw species
    color = RED if species["data"]["type"] == "invasive" else GREEN
    pygame.draw.rect(screen, color, species["rect"])

    # HUD
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Lives: {lives}", 10, 40)
    draw_text("Touch species + press SPACE", 10, 70)

    if message_timer > 0:
        draw_text(message, 200, 550)
        message_timer -= 1

    # Win / lose conditions
    if score >= 5:
        game_over = True
        win = True

    if lives <= 0:
        game_over = True

    if game_over:
        if win:
            draw_text("YOU WIN!", 320, 250, GREEN, big=True)
            draw_text("You protected the ecosystem!", 250, 300)
        else:
            draw_text("GAME OVER", 300, 250, RED, big=True)
            draw_text("Native species were harmed.", 240, 300)

    pygame.display.flip()

pygame.quit()
sys.exit()
