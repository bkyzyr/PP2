import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)

background = pygame.image.load("clock.png")
right_hand = pygame.image.load("rightarm.png")
left_hand = pygame.image.load("leftarm.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

right_hand_rect = right_hand.get_rect()
left_hand_rect = left_hand.get_rect()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey clock")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = - (minutes % 60) * 6
    second_angle = - (seconds % 60) * 6

    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)
    
    right_hand_rect = rotated_right_hand.get_rect(center=CENTER)
    left_hand_rect = rotated_left_hand.get_rect(center=CENTER)
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(rotated_right_hand, right_hand_rect.topleft)
    screen.blit(rotated_left_hand, left_hand_rect.topleft)
    
    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
