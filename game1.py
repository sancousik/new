import pygame

window = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("HELLO PYGAME!")

screen = pygame.Surface((1000,1000))

square = pygame.Surface((50,50))
square.fill((255,0,0))
square_go_right = True

x = 0

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    x += 1
    screen.fill((0, 255, 255))
    if square_go_right == True:
        x += 1
        if x >= 950:
            square_go_right = False
    elif square_go_right == False:
        x -= 1
        if x <= 50:
            square_go_right = True

    screen.blit(square, (x,0))
    window.blit(screen,(0,0))
    pygame.display.flip()
