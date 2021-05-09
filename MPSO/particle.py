from .config import dimensions, domain, c1, c2, w, calculate_value
from random import random


class Particle:
    def __init__(self):
        self.coordinates = []
        self.velocity = []
        self.best = []

        for i in range(0, dimensions):
            self.coordinates.append(random() * domain * 2 - domain)
            self.velocity.append(random() * 2 - 1)
        self.best = self.coordinates

    def move(self, global_best, lbest):
        for i in range(0, len(self.coordinates)):
            if self == lbest:
                continue
            self.update_velocity(global_best, i)
            self.update_position(i)
        self.set_new_best()

    def update_velocity(self, global_best, i):
        r1 = random()
        r2 = random()
        cognitive_velocity = c1 * r1 * (self.best[i] - self.coordinates[i])
        social_velocity = c2 * r2 * (global_best[i] - self.coordinates[i])
        self.velocity[i] = w * self.velocity[i] + cognitive_velocity + social_velocity

    def update_position(self, i):
        self.coordinates[i] += self.velocity[i]

    def set_new_best(self):
        if (calculate_value(self.coordinates) < calculate_value(self.best)) and abs(
                max(self.coordinates)) <= domain and abs(min(self.coordinates) <= domain):
            self.best = self.coordinates
