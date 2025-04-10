import pygame
import random
from game_object import GameObject, Point
import os

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 300
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
speed = 5 
class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__([], (255, 0, 0), tile_width)  # WALL_COLOR
        self.level = 1
        self.load_level()
    
    def load_level(self):
        self.points = []
        level_file = f"levels/level{self.level}.txt"
        if os.path.exists(level_file):
            with open(level_file, "r") as f:
                row = -1
                for line in f:
                    row += 1
                    col = -1
                    for c in line:
                        col += 1
                        if c == '#':
                            self.points.append((col * self.tile_width, row * self.tile_width))
        else:
            print(f"Level {self.level} file not found! Staying on the current level.")
    
    def next_level(self):
        next_level = self.level + 1
        if os.path.exists(f"levels/level{next_level}.txt"):
            self.level = next_level
            self.load_level()
        else:
            print("No more levels available. Staying on the current level.")

wall = Wall(CELL_SIZE)

snake = [(40, 40)]
dx, dy = 1, 0

def generate_food():
    while True:
        food_position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if food_position not in snake and food_position not in wall.points:
            return food_position

food = generate_food()

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
    
    if new_head in wall.points:
        snake = [(40, 40)]
        dx, dy = 1, 0
        score = 0
        level = 1
        speed = 5
        wall.load_level()
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 1
            wall.next_level()
        food = generate_food()
    else:
        snake.pop()
    
    screen.fill((0, 0, 0))  # BACKGROUND_COLOR
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (207, 203, 192), (x, 0), (x, HEIGHT))  # GRID_COLOR
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (207, 203, 192), (0, y), (WIDTH, y))  # GRID_COLOR
    
    for point in wall.points:
        pygame.draw.rect(screen, (255, 0, 0), (*point, CELL_SIZE, CELL_SIZE))  # WALL_COLOR
    
    for segment in snake:
        pygame.draw.rect(screen, (12, 237, 211), (*segment, CELL_SIZE, CELL_SIZE))  # SNAKE_COLOR
    
    pygame.draw.rect(screen, (237, 12, 75), (*food, CELL_SIZE, CELL_SIZE))  # FOOD_COLOR
    
    font = pygame.font.Font(None, 24)
    text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()