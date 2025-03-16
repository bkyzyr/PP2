import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (255, 255, 255)  # White
STEP = 20  # Movement step size

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moveable Red Ball")

# Ball initial position (centered)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Main loop
running = True
while running:
    pygame.time.delay(50)  # Delay for smooth movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - STEP >= 0:
                ball_y -= STEP
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + STEP <= HEIGHT:
                ball_y += STEP
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - STEP >= 0:
                ball_x -= STEP
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + STEP <= WIDTH:
                ball_x += STEP
    
    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.update()

pygame.quit()