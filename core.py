import random
import math
import time


def create_state(n):
    state = list(range(n))
    random.shuffle(state)
    return state


def cost_function(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost


def neighbor(state):
    new = state.copy()
    i, j = random.sample(range(len(new)), 2)
    new[i], new[j] = new[j], new[i]
    return new


def simulated_annealing(n, cooling, T_start=100, max_steps=1000):
    current = create_state(n)
    current_cost = cost_function(current)

    steps = 0

    while steps < max_steps:

        if current_cost == 0:
            return steps, True, current_cost

        new = neighbor(current)
        new_cost = cost_function(new)
        delta = new_cost - current_cost

        T = T_start * (cooling ** steps)

        if delta < 0 or (T > 0 and random.random() < math.exp(-delta / T)):
            current = new
            current_cost = new_cost

        steps += 1

    return steps, current_cost == 0, current_cost