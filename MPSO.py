from MPSO.swarm import Swarm
from MPSO.config import swarms_number, iterations, calculate_value, shuffle_iterations
import math
from random import shuffle

def update_leaders():
    leaders = []
    for swarm in swarms:
        leaders.append(swarm.lbest)
    return leaders


def calculate_mean(leaders):
    sum = 0.0
    count = 0.0
    for leader in leaders:
        for coordinate in leader.coordinates:
            sum += coordinate
            count += 1
    return sum/count

def shuffle_swarms():
    print("Shuffling...")
    all_particles = []
    for swarm in swarms:
        for particle in swarm.particles:
            all_particles.append(particle)
    shuffle(all_particles)
    for swarm in swarms:
        for i in range(0, len(swarm.particles)):
            swarm.particles[i] = all_particles.pop()


swarms = []
for i in range(0, swarms_number):
    swarms.append(Swarm())

best = math.inf
for i in range(0, iterations):
    if i % shuffle_iterations == 0:
        shuffle_swarms()
    mean = calculate_mean(update_leaders())
    for swarm in swarms:
        swarm.move()
        swarm.move_leader(mean)
        if calculate_value(swarm.best) < best:
            best = calculate_value(swarm.best)
    print("Iteration {}, best: {}".format(i, best))
