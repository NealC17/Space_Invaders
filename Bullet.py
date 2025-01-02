import pygame
from PyVector import PyVector
class Bullet:
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
        self.dead = False

    def move(self):
        self.pos.add(self.vel.x, self.vel.y, 0)

    def draw(self, screen):
        screen.blit(self.shape, (self.pos.x, self.pos.y))

    def checkCollision(self, bullet):
        if bullet.pos.x < self.pos.x < bullet.pos.x + bullet.shape.get_size()[0] and bullet.pos.y < self.pos.y < bullet.pos.y + bullet.shape.get_size()[1]:
            self.dead = True
        pass


