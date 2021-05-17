import math
import numpy as np
mark = "corana"

population = 35
dimensions = 20
domain = 10
iterations = 300

a_max = 1
a = 0.5
c = 0.5
p = 0.3

precision = 0.001
is_precision = False

def calculate_value(coordinates):
    return sphere(coordinates)


def sphere(coordinates):
    total = 0
    for i in coordinates:
        total += pow(i, 2)
    return total


def rastrigin(coordinates):
    total = 0
    for c in coordinates:
        total += pow(c, 2) - 10 * math.cos(2 * math.pi * c)
    return total + 10 * dimensions


def rosenbrock(coordinates):
    total = 0
    for i in range(0, len(coordinates) - 1):
        total += 100 * pow(coordinates[i + 1] - pow(coordinates[i], 2), 2) + pow(coordinates[i] - 1, 2)
    return total


def brown(coordinates):
    total = 0
    for i in range(0, len(coordinates) - 1):
        total += 100 * pow(pow(coordinates[i], 2), pow(coordinates[i + 1], 2) + 1) + pow(pow(coordinates[i + 1], 2),
                                                                                         pow(coordinates[i], 2) + 1)
    return total


def corana(coordinates):
    total = 0
    d = [1, 1000, 10, 100]
    for i in range(0, 3):
        z = math.floor(abs(coordinates[i] / 0.2) + 0.49999) * np.sign(coordinates[i]) * 0.2
        if abs(coordinates[i] - z) < 0.05:
            total += 0.15 * pow(z - 0.05 * np.sign(z), 2) * d[i]
        else:
            total += d[i] * pow(coordinates[i], 2)
    return total
