import pygame, sys
pygame.init
size = width, height = 750, 750
screen = pygame.display.set_mode(size)
def render(sprite, x ,y):
    sprite = pygame.image.load(sprite)
    screen.blit(sprite, (x, y))
screen.fill((255,255,255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.display.flip()
    render("./Letters/A", 300, 300)
    render("./Letters/B", 320, 300)
    render("./Letters/B", 340, 300)
    render("./Letters/A", 360, 300)
    
