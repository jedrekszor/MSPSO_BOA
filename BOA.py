from BOA.butterfly import Butterfly
from BOA.config import population, iterations, calculate_value, mark, a, a_max, precision, is_precision
import math
import matplotlib.pyplot as plt
import os
import time

swarm = []
for i in range(0, population):
    swarm.append(Butterfly())

start_time = time.time()
global_best = math.inf
results = []
for i in range(0, iterations):
    results.append(0)
for j in range(0, 30):
    best = math.inf
    if is_precision:
        if best < precision:
            break
    for i in range(0, iterations):
        best_butterfly = swarm[0]
        for butterfly in swarm:
            butterfly.calculate_fragrance()
            if butterfly.fragrance > best_butterfly.fragrance:
                best_butterfly = butterfly
        av = 0
        for butterfly in swarm:
            butterfly.move(best_butterfly, swarm)
            av += calculate_value(butterfly.coordinates)
        if calculate_value(best_butterfly.coordinates) < best:
            best = calculate_value(best_butterfly.coordinates)
            if best < global_best:
                global_best = best
        # a = a_max * (1 - (i/iterations)/2)
        results[i] += best
        print("Cycle: {}, Iteration {}, best value: {}".format(j, i, best))
    print("################################")
for i in range(0, iterations):
    results[i] = results[i]/30
plt.plot(results)
if not os.path.isdir("raport/plots/BOA"):
    os.makedirs("raport/plots/BOA")
plt.savefig("raport/plots/BOA/{}.png".format(mark))
print("\nPlots saved, overall best: {}".format(global_best))
delta = time.time() - start_time
print("Execution time: {}m {}s".format(int(delta / 60), delta % 60))
