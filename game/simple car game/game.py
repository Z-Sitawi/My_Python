import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (80, 220, 255)
RED = (255, 0, 0)
CAR_WIDTH, CAR_HEIGHT = 100, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
OBSTACLE_SPEED = 13
MAX_LEVEL = 10

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Car Game")

# Load images and sounds
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

obstacle_image = pygame.image.load("rock.png")
obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (40, 40))

explosion_sound = pygame.mixer.Sound("boom.wav")
coin_sound = pygame.mixer.Sound("coinsound.wav")

# Car attributes
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20
car_speed = 8

# Obstacle attributes
obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
obstacle_y = -OBSTACLE_HEIGHT
obstacle_speed = OBSTACLE_SPEED

# Coin attributes
coin_x = random.randint(0, WIDTH - 40)
coin_y = -40
coin_speed = 8
coin_collected = False

# Score and Level
score = 0
level = 1
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += car_speed

    # Move the obstacle
    obstacle_y += obstacle_speed

    # Move the coin
    coin_y += coin_speed

    # Check for collision with obstacles
    if (car_x < obstacle_x + OBSTACLE_WIDTH and car_x + CAR_WIDTH > obstacle_x and car_y < obstacle_y + OBSTACLE_HEIGHT
            and car_y + CAR_HEIGHT > obstacle_y):
        pygame.mixer.Sound.play(explosion_sound)
        running = False

    # Check for collision with coin
    if (not coin_collected and car_x < coin_x + 40 and car_x + CAR_WIDTH > coin_x and car_y < coin_y + 40 and car_y +
            CAR_HEIGHT > coin_y):
        pygame.mixer.Sound.play(coin_sound)
        coin_collected = True
        score += 10

    # Spawn a new obstacle when it goes off-screen
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        obstacle_y = -OBSTACLE_HEIGHT

    # Spawn a new coin when it goes off-screen
    if coin_y > HEIGHT:
        coin_x = random.randint(0, WIDTH - 40)
        coin_y = -40
        coin_collected = False

    # Update level
    if score >= level * 30 and level < MAX_LEVEL:
        level += 1
        obstacle_speed += 1
        coin_speed += 0.5

    # Clear the screen
    screen.fill(WHITE)

    # Draw the car
    screen.blit(car_image, (car_x, car_y))

    # Draw the obstacle
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Draw the coin
    screen.blit(coin_image, (coin_x, coin_y))

    # Display the score and level
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f"Level: {level}", True, RED)
    screen.blit(level_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Game over screen
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect.topleft)
pygame.display.flip()
pygame.time.delay(2000)  # Pause for 2 seconds before exiting

# Quit the game
pygame.quit()
sys.exit()