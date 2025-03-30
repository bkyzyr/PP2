import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 300
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

SNAKE_COLOR = (12, 237, 211)
FOOD_COLOR = (237, 12, 75)
GRID_COLOR = (207, 203, 192)
BACKGROUND_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
speed = 5

snake = [(40, 40)]
dx, dy = 1, 0

food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

score = 0
level = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0

    new_head = (snake[0][0] + dx * CELL_SIZE, snake[0][1] + dy * CELL_SIZE)
    
    if new_head[0] < 0:
        new_head = (WIDTH - CELL_SIZE, new_head[1])
    elif new_head[0] >= WIDTH:
        new_head = (0, new_head[1])
    if new_head[1] < 0:
        new_head = (new_head[0], HEIGHT - CELL_SIZE)
    elif new_head[1] >= HEIGHT:
        new_head = (new_head[0], 0)
    
    if new_head in snake:
        snake = [(40, 40)]
        dx, dy = 1, 0
        score = 0
        level = 1
        speed = 5
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 1
        while True:
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            if food not in snake:
                break
    else:
        snake.pop()
    
    screen.fill(BACKGROUND_COLOR)
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))
    
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, FOOD_COLOR, (*food, CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.Font(None, 24)
    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
