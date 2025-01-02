import pygame
from PyVector import PyVector
from Bullet import Bullet
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


