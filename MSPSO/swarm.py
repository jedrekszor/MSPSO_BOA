from .config import population, calculate_value
from .particle import Particle

class Swarm:
    def __init__(self):
        self.coordinates = []
        self.particles = []
        self.best = []

        for i in range(0, len(population)):
            self.particles.append(Particle())
        self.best = self.particles[0]
        self.set_new_best()

    def move(self):
        for particle in self.particles:
            particle.move(self.best)

    def set_new_best(self):
        for particle in self.particles:
            if calculate_value(particle.best) < calculate_value(self.best):
                self.best = particle