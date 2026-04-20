import random
import math
import time
import pygame
from core import create_state, cost_function, neighbor


def draw_board(screen, state, size):
    n = len(state)
    cell = size // n

    screen.fill((255, 255, 255))

    for row in range(n):
        for col in range(n):
            color = (240, 240, 240) if (row + col) % 2 == 0 else (100, 100, 100)
            pygame.draw.rect(screen, color, (col * cell, row * cell, cell, cell))

            if state[col] == row:
                cx = col * cell + cell // 2
                cy = row * cell + cell // 2
                pygame.draw.circle(screen, (255, 0, 0), (cx, cy), cell // 3)

    pygame.display.flip()


def run_visual(state):
    pygame.init()

    size = 600
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Simulated Annealing N-Queens")

    current = state
    current_cost = cost_function(current)

    T = 100
    start = time.time()
    steps = 0

    running = True

    while running and T > 0.001:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_cost == 0:
            break

        new = neighbor(current)
        new_cost = cost_function(new)
        delta = new_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new
            current_cost = new_cost

        T *= 0.99
        steps += 1

        draw_board(screen, current, size)
        pygame.time.delay(1)

    print("Final cost:", current_cost)
    print("Steps:", steps)
    print("Time:", time.time() - start)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    n = int(input("n: "))
    state = create_state(n)
    run_visual(state)