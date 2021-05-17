from .config import dimensions, domain, c, a, calculate_value, p
from random import random, choice


class Butterfly:
    def __init__(self):
        self.fragrance = None
        self.coordinates = []

        for i in range(0, dimensions):
            self.coordinates.append(random() * domain * 2 - domain)

    def calculate_fragrance(self):
        I = 1 / calculate_value(self.coordinates)
        self.fragrance = c * pow(I, a)

    def move(self, best_butterfly, butterflies):
        r = random()
        if r < p:
            for i in range(0, len(self.coordinates)):
                self.coordinates[i] += (pow(r, 2) * best_butterfly.coordinates[i] - self.coordinates[
                    i]) * self.fragrance
        else:
            r1 = choice(butterflies)
            r2 = choice(butterflies)
            for i in range(0, len(self.coordinates)):
                self.coordinates[i] += (pow(r, 2) * r1.coordinates[i] - r2.coordinates[i]) * self.fragrance
