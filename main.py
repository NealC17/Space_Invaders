import sys
from random import random

import pygame
from PyVector import PyVector
from Bullet import Bullet
from Alien import Alien


class Ship:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.shape.fill(color)
        self.color = color
        self.pos = PyVector()
        self.pos.x = x
        self.pos.y = y
        self.vel = PyVector()
        self.vel.x = 5
        self.vel.y = 0
        self.bullets = []
        self.dead = False

    # direction is +1 ( right), 0 (not moving), or -1 (left)
    def move(self, direction):
        if self.dead:
            return
        tempVel = self.vel.mult(direction)
        self.pos.add(tempVel.x, tempVel.y, 0)

        if self.pos.x + self.shape.get_size()[0] > 800:
            self.pos.x = 800- self.shape.get_size()[0]

        if self.pos.x <0:
            self.pos.x =0

        for e in self.bullets:
            e.move()
            if(e.dead or e.pos.y < -50):
                self.bullets.remove(e)

    def draw(self, screen):
        for e in self.bullets:
            e.draw(screen)
        screen.blit(self.shape, (self.pos.x, self.pos.y))

    def shoot(self):
        if self.dead:
            return
        surface = pygame.Surface([10, 20])
        b = Bullet(surface, (255, 255, 255), self.pos.x + self.shape.get_size()[0] / 2 - surface.get_size()[0] / 2,
                   self.pos.y, -10)
        self.bullets.append(b)

        for i in range(0, len(self.bullets)):
            if len(self.bullets) > i > -1 and self.bullets[i].pos.y < 0:
                self.bullets.remove(self.bullets[i])
                i -= 1

    def checkCollision(self, bullet):
        if bullet.pos.x < self.pos.x < bullet.pos.x + bullet.shape.get_size()[0] and bullet.pos.y < self.pos.y < bullet.pos.y + bullet.shape.get_size()[1]:
            self.dead = True
            self.bullets = []
        pass


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
