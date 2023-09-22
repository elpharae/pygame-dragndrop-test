import pygame
import time

pygame.init()

width, height = (640, 400)
running = True
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

gap = width / 10 
padding = gap / 2 
# amount of viable slots = (int(width / gap) - 1) * (int(height / gap) - 1) 
slots_count = (int(width / gap) - 1) * (int(height / gap) - 1)
slot_positions = []
printed = False


for x in range(0, int(width / gap) - 1):
    for y in range(0, int(height / gap) - 1):
        slot_positions.append((2 * padding + x * gap, 2 * padding + y * gap))

item = pygame.Rect(0, 0, 50, 50)
item_position = slot_positions[4]
item_holding = False


previous_time = time.time() * 1000
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if item.collidepoint(event.pos) :
                    item_holding = True
                    
        if event.type == pygame.MOUSEMOTION:
            if item_holding:
                item_position = (item_position[0] + event.rel[0], item_position[1] + event.rel[1])

        if event.type == pygame.MOUSEBUTTONUP:
            item_holding = False
            v2 = pygame.math.Vector2(item_position[0], item_position[1])
            min = 10000000 
            pos = ()
            for x, y in slot_positions:
                v1 = pygame.math.Vector2(x, y)
                distance = v1.distance_to(v2)
                if distance < min:
                    min = distance
                    pos = (x, y)
            item_position = pos 

    screen.fill("black")

    for x, y in slot_positions: 
        pygame.draw.circle(screen, "white", (x, y), radius=2, width=2)

    for x in range(0, int(width / gap)):
        pygame.draw.line(screen, "white", (padding + x * gap, 0), (padding + x * gap, height), width=1)
    for x in range(0, int(height / gap)):
        pygame.draw.line(screen, "white", (0, padding + x * gap), (width, padding + x * gap), width=1)
        
    item.center = item_position
    pygame.draw.rect(screen, "red", item)

    pygame.display.update()

pygame.quit()