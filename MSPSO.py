from MSPSO.swarm import Swarm
from MSPSO.config import swarms_number, iterations, calculate_value
import math


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


swarms = []
for i in range(0, swarms_number):
    swarms.append(Swarm())

best = math.inf
for i in range(0, iterations):
    mean = calculate_mean(update_leaders())
    for swarm in swarms:
        swarm.move()
        swarm.move_leader(mean)
        if calculate_value(swarm.best) < best:
            best = calculate_value(swarm.best)
    print("Iteration {}, best: {}".format(i, best))
