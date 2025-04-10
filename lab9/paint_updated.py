import pygame 

WIDTH, HEIGHT = 1200, 800 
FPS = 90
draw = False          
radius = 15 
color = 'blue'           
mode = 'pen'                

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint') 
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
font = pygame.font.SysFont('None', 60) 

def drawLine(screen, start, end, width, color): 
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    if dx > dy: 
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for x in range(x1, x2): 
            y = int((-C - A * x) / B)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    else: 
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        for y in range(y1, y2): 
            x = int((-C - B * y) / A)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

def drawCircle(screen, start, end, width, color): 
    x1, y1 = start
    x2, y2 = end
    x = (x1 + x2) // 2 
    y = (y1 + y2) // 2 
    radius = abs(x1 - x2) // 2 
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)

def drawRectangle(screen, start, end, width, color): 
    x1, y1 = start
    x2, y2 = end
    widthr = abs(x1 - x2) 
    height = abs(y1 - y2) 
    rect = pygame.Rect(min(x1, x2), min(y1, y2), widthr, height)
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def drawSquare(screen, start, end, color): 
    x1, y1 = start
    x2, y2 = end
    mn = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, mn, mn)
    if x2 < x1:
        rect.x = x1 - mn
    if y2 < y1:
        rect.y = y1 - mn
    pygame.draw.rect(screen, pygame.Color(color), rect)

def drawRightTriangle(screen, start, end, color): 
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, pygame.Color(color), [(x1, y1), (x1, y2), (x2, y2)])

def drawEquilateralTriangle(screen, start, end, width, color): 
    x1, y1 = start
    x2, y2 = end
    base_width = abs(x2 - x1)
    height = (3**0.5) * base_width / 2
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), [
            (x1, y2), 
            (x2, y2), 
            ((x1 + x2) / 2, y2 - height)
        ], width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), [
            (x1, y1), 
            (x2, y1), 
            ((x1 + x2) / 2, y1 - height)
        ], width)

def drawRhombus(screen, start, end, width, color): 
    x1, y1 = start
    x2, y2 = end
    points = [
        ((x1 + x2) / 2, y1),
        (x1, (y1 + y2) / 2),
        ((x1 + x2) / 2, y2),
        (x2, (y1 + y2) / 2)
    ]
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_r: mode = 'rectangle'  
            if event.key == pygame.K_c: mode = 'circle' 
            if event.key == pygame.K_p: mode = 'pen'
            if event.key == pygame.K_e: mode = 'erase'
            if event.key == pygame.K_s: mode = 'square' 
            if event.key == pygame.K_t: mode = 'right_tri'
            if event.key == pygame.K_u: mode = 'eq_tri'  
            if event.key == pygame.K_h: mode = 'rhombus'  
            if event.key == pygame.K_q: screen.fill(pygame.Color('white')) 
            if event.key == pygame.K_1: color = 'black'
            if event.key == pygame.K_2: color = 'green' 
            if event.key == pygame.K_3: color = 'red'
            if event.key == pygame.K_4: color = 'blue'
            if event.key == pygame.K_5: color = 'yellow'
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True 
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos 
        if event.type == pygame.MOUSEBUTTONUP:  
            if mode == 'rectangle': drawRectangle(screen, prevPos, event.pos, radius, color)  
            elif mode == 'circle': drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square': drawSquare(screen, prevPos, event.pos, color)  
            elif mode == 'right_tri': drawRightTriangle(screen, prevPos, event.pos, color)
            elif mode == 'eq_tri': drawEquilateralTriangle(screen, prevPos, event.pos, radius, color) 
            elif mode == 'rhombus': drawRhombus(screen, prevPos, event.pos, radius, color) 
            draw = False  
        if event.type == pygame.MOUSEMOTION:  
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color) 
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = font.render(str(radius), True, pygame.Color(color)) 
    screen.blit(renderRadius, (5, 5))
    pygame.display.flip()
    clock.tick(FPS)