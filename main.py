import pygame
from pygame.locals import *
import os, sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    bckgd = pygame.Surface(screen.get_size())
    bckgd = bckgd.convert()
    bckgd.fill((150, 150, 150))
    logo = load_image('LOGO.png')
    logo_final = pygame.transform.scale(logo[0], (500,800))

    font = pygame.font.Font(None, 36)
    text = font.render("LINDMOR Industries", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = bckgd.get_rect().centerx
    textpos.centery = bckgd.get_rect().centery
    bckgd.blit(text, textpos)

    screen.blit(bckgd, (0, 0))
    screen.blit(logo_final, (100, 100))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            screen.blit(bckgd, (0, 0))

            pygame.display.flip()


def load_image(name):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:' + fullname)
        raise SystemExit(message)
    return image, image.get_rect()


if __name__ == "__main__":
    main()
