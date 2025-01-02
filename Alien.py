from PyVector import PyVector
from Bullet import Bullet
from random import random
import pygame

class Alien:
    def __init__(self, shape, color, x, y, velY):
        self.shape = shape
        self.shape.fill(color)
        self.color = color
        self.pos = PyVector()
        self.pos.x = x
        self.pos.y = y
        self.vel = PyVector()
        self.vel.x = 0
        self.vel.y = velY
        self.acc = []
        self.bullets = []
        self.index = 0
        self.dead = False

        for i in range(1000):
            self.acc.append(PyVector())
            self.acc[i].x = random() - 0.5
            self.acc[i].y = random() - 0.5
            self.acc[i].scale(1)

    def move(self):
        self.pos.add(self.vel.x, self.vel.y, 0)
        temp = self.acc[self.index % len(self.acc)]
        self.vel.add(temp.x, temp.y, temp.z)
        self.index += 1

        if self.index % 30 == 0:
            self.shoot()

    def draw(self, screen):
        screen.blit(self.shape, (self.pos.x, self.pos.y))
        for e in self.bullets:
            e.move()
            e.draw(screen)
            if(e.dead):
                self.bullets.remove(e)

    def shoot(self):
        surface = pygame.Surface([10, 20])
        b = Bullet(surface, (10, 255, 255), self.pos.x + self.shape.get_size()[0] / 2 - surface.get_size()[0] / 2,
                   self.pos.y, 10)
        self.bullets.append(b)
        for i in range(0, len(self.bullets)):
            if -1 < i < len(self.bullets) and self.bullets[i].pos.y > 800:
                self.bullets.remove(self.bullets[i])

    def checkCollision(self, bullet):
        if bullet.pos.x < self.pos.x < bullet.pos.x + bullet.shape.get_size()[0] and bullet.pos.y < self.pos.y < bullet.pos.y + bullet.shape.get_size()[1]:
            self.dead = True
        pass





