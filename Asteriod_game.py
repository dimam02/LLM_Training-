import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Asteroid Game")

# Define colors
WHITE = (255, 255, 255)

# Load game assets
spaceship_img = pygame.image.load("spaceship.png")
asteroid_img = pygame.image.load("asteroid.png")
bullet_img = pygame.image.load("bullet.png")

# Resize game assets
spaceship_img = pygame.transform.scale(spaceship_img, (64, 64))
asteroid_img = pygame.transform.scale(asteroid_img, (64, 64))
bullet_img = pygame.transform.scale(bullet_img, (32, 32))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game variables
spaceship_x = screen_width // 2
spaceship_y = screen_height - 100
spaceship_speed = 5

bullets = []
bullet_speed = 10

asteroids = []
asteroid_speed = 3

score = 0
font = pygame.font.Font(None, 36)

game_over = False

# Game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship_x -= spaceship_speed
            if event.key == pygame.K_RIGHT:
                spaceship_x += spaceship_speed
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(spaceship_x + 16, spaceship_y, 8, 16)
                bullets.append(bullet)

    # Update game logic
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    for asteroid in asteroids:
        asteroid.y += asteroid_speed
        if asteroid.y > screen_height:
            asteroids.remove(asteroid)
            score -= 1

    if len(asteroids) < 10:
        if random.randint(0, 100) < 5:
            asteroid_x = random.randint(0, screen_width - 64)
            asteroid = pygame.Rect(asteroid_x, -64, 64, 64)
            asteroids.append(asteroid)

    for asteroid in asteroids:
        if asteroid.colliderect(pygame.Rect(spaceship_x, spaceship_y, 64, 64)):
            game_over = True

        for bullet in bullets:
            if bullet.colliderect(asteroid):
                asteroids.remove(asteroid)
                bullets.remove(bullet)
                score += 1

    # Render game graphics
    screen.fill(WHITE)

    for bullet in bullets:
        screen.blit(bullet_img, (bullet.x, bullet.y))

    for asteroid in asteroids:
        screen.blit(asteroid_img, (asteroid.x, asteroid.y))

    screen.blit(spaceship_img, (spaceship_x, spaceship_y))

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the game display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

# Game over
game_over_text = font.render("Game Over", True, (255, 0, 0))
screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 20))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit the game
pygame.quit()