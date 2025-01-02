import sys
from random import random

import pygame
from PyVector import PyVector
from Bullet import Bullet
from Alien import Alien
from Ship import Ship


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    shape = pygame.Surface([30, 30])
    aliens = [Alien(pygame.Surface([30, 15]), (25, 155, 25), 400, 0, 5)]
    ship = Ship(shape, (10, 10, 165), 400, 450)
    while running:
        direction = 0;
        if random() < 0.1:
            aliens.append(Alien(pygame.Surface([30, 15]), (25, 155, 25), int(random() * 800), 0, 5))
        keys = pygame.key.get_pressed()

        for e in aliens:
            for i in ship.bullets:
                e.checkCollision(i)

            for k in e.bullets:
                ship.checkCollision(bullet=k)

            for j in ship.bullets:
                for l in e.bullets:
                    j.checkCollision(l)
                    l.checkCollision(j)

        if keys[pygame.K_RIGHT]:
            direction = 1
        if keys[pygame.K_LEFT]:
            direction = -1
        if keys[pygame.K_SPACE]:
            ship.shoot()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(0, len(aliens)):
            if -1 < i < len(aliens) and aliens[i] in aliens and aliens[i].pos.y > 800:
                aliens.remove(aliens[i])
                i -= 1;

            if -1 < i < len(aliens) and aliens[i] in aliens and aliens[i].dead:
                aliens.remove(aliens[i])
                i -= 1;

        ship.move(direction)
        screen.fill((0, 0, 0))
        ship.draw(screen)
        for e in aliens:
            e.move()
            e.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
