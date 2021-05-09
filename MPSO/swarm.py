from .config import population, calculate_value
from .particle import Particle
from random import random


class Swarm:
    def __init__(self):
        self.coordinates = []
        self.particles = []
        self.best = []
        self.lbest = None
        for i in range(0, population):
            self.particles.append(Particle())
        self.best = self.particles[0].coordinates
        self.lbest = self.particles[0]
        self.set_new_best()

    def move(self):
        for particle in self.particles:
            particle.move(self.best, self.lbest)
            self.set_new_best()

    def set_new_best(self):
        for particle in self.particles:
            if calculate_value(particle.coordinates) < calculate_value(self.lbest.coordinates):
                self.lbest = particle
            if calculate_value(particle.best) < calculate_value(self.best):
                self.best = particle.coordinates

    def move_leader(self, mean):
        for c in self.lbest.coordinates:
            c = mean * (1 + random())
