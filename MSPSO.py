from MSPSO.swarm import Swarm
from MSPSO.config import swarms_number, iterations, calculate_value, mark, w_max, w_min, c1_fin, \
    c2_fin, c1_init, c2_init, precision, is_precision
import MSPSO.config as cfg
import math
import matplotlib.pyplot as plt
import os
import time


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
    return sum / count


def adjust_acceleration(i):
    cfg.w = w_min + (w_max - w_min) * (iterations - i) / iterations
    cfg.c1 = (c1_fin - c1_init) * (i / iterations) + c1_init
    cfg.c2 = (c2_fin - c2_init) * (i / iterations) + c2_init


def init_swarms():
    swarms.clear()
    for sw in range(0, swarms_number):
        swarms.append(Swarm())


swarms = []

start_time = time.time()
global_best = math.inf
results = []
for i in range(0, iterations):
    results.append(0)
for j in range(0, 30):
    init_swarms()
    best = math.inf
    if is_precision:
        if best < precision:
            break
    cfg.w = w_max
    cfg.c1 = c1_init
    cfg.c2 = c2_init
    for i in range(0, iterations):
        mean = calculate_mean(update_leaders())
        for swarm in swarms:
            swarm.move()
            swarm.move_leader(mean)
            if calculate_value(swarm.best) < best:
                best = calculate_value(swarm.best)
                if best < global_best:
                    global_best = best
        adjust_acceleration(i)
        results[i] += best
        print("Cycle: {}, Iteration {}, best: {}".format(j, i, best))
    print("################################")
for i in range(0, iterations):
    results[i] = results[i] / 30
plt.plot(results)
if not os.path.isdir("../raport/plots/MSPSO"):
    os.makedirs("../raport/plots/MSPSO")
plt.savefig("../raport/plots/MSPSO/{}.png".format(mark))
print("\nPlot saved, overall best: {}".format(global_best))
delta = time.time() - start_time
print("Execution time: {}m {}s".format(int(delta / 60), delta % 60))
