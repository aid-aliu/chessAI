import pygame
from pygame import Surface

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

cellSize = 20
board = Surface((cellSize * 8, cellSize * 8))
board.fill((255, 255, 255))
for x in range(0, 8):
    for y in range(0, 8):
        if  x % 2 == 0:
            if y % 2 == 0:
                pygame.draw.rect(board, (255, 255, 255), (x * cellSize, y * cellSize, cellSize, cellSize))
            else:
                pygame.draw.rect(board, (0, 0, 0), (x * cellSize, y * cellSize, cellSize, cellSize))
        else:
            if y % 2 != 0:
                pygame.draw.rect(board, (255, 255, 255), (x * cellSize, y * cellSize, cellSize, cellSize))
            else:
                pygame.draw.rect(board, (0, 0, 0), (x * cellSize, y * cellSize, cellSize, cellSize))



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.blit(board, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()