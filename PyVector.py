from math import *


class PyVector:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def clone(self):
        return PyVector(self.x, self.y, self.z)

    def scale(self, c):
        self.x *= c
        self.y *= c
        self.z *= c

    def mult(self, c):
        out = PyVector()
        out.x = c * self.x
        out.y = c * self.y
        out.z = c * self.z
        return out

    def add(self, pVector):
        self.add(pVector.x, pVector.y, pVector.z)

    def add(self, x, y):
        self.add(x, y, 0)

    def add(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def mag(self):
        return sqrt(self.magSq())

    def magSq(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def norm(self):
        m = self.mag()
        self.x /= m
        self.y /= m
        self.z /= m

    def dot(self, pVector):
        return self.dot(pVector.x, pVector.y, pVector.z)

    def dot(self, x, y, z):
        return self.x * x + self.y * y + self.z * z

    def cross(self, pVector):
        return self.cross(pVector.x, pVector.y, pVector.z)

    def cross(self, x, y, z):
        return PyVector(self.y * z - self.z * y, -self.x * z + self.z * x, self.x * y - self.y * x)

    # the angle made by the vector in the xy plane 0 < theta < 2 pi
    def theta(self):
        return atan(self.y / self.x)

    # the angle made between the vector and the z axis 0 < phi < pi
    def phi(self):
        return acos(self.z / self.mag())

    # rotation in the xy plane
    def rotateXY(self, delta_theta):
        theta = self.theta()
        mag = self.mag()

        theta += delta_theta
        self.x = mag * acos(theta)
        self.y = mag * asin(theta)
