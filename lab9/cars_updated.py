import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Set up the frame rate
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up screen size and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COINS = 0
COIN_SPEEDUP_THRESHOLD = 10  # Increase enemy speed every 10 coins

# Set up fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class with random weights
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        self.value = random.choice([1, 2, 3])  # Assign random weight

    def reset_position(self):
        # Move coin to a new random location
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
        self.value = random.choice([1, 2, 3])  # Assign new weight

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Instantiate game objects
P1 = Player()
E1 = Enemy()
coin_list = [Coin() for _ in range(3)]  # Multiple coins

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coinss = pygame.sprite.Group()
coinss.add(*coin_list)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coin_list)

# Custom event to increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Function to handle crash
def handle_crash():
    time.sleep(2)

background_y = 0

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        handle_crash()
        pygame.quit()
        sys.exit()

    # Scroll background
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Display score and coin count
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coins = font_small.render("Coins: " + str(COINS), True, BLACK)
    screen.blit(coins, (SCREEN_WIDTH - 100, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Coin):
            entity.rect.y += SPEED
            if pygame.sprite.collide_rect(P1, entity):
                COINS += entity.value
                entity.reset_position()
                # Increase enemy speed every N coins
                if COINS % COIN_SPEEDUP_THRESHOLD == 0:
                    SPEED += 0.5
            elif entity.rect.top > SCREEN_HEIGHT:
                entity.reset_position()
        elif isinstance(entity, Enemy):
            entity.move()
        elif isinstance(entity, Player):
            entity.move()

    # Refresh the screen
    pygame.display.update()
    FramePerSec.tick(FPS)
