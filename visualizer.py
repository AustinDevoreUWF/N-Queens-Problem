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
                cx = int(col * cell + cell // 2)
                cy = int(row * cell + cell // 2)
                pygame.draw.circle(screen, (255, 0, 0), (cx, cy), cell // 3)
    pygame.display.flip()

def run_visual(state):
    pygame.init()
    size = 600
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("N-Queens Simulated Annealing")

    current = state
    current_cost = cost_function(current)
    T = 100
    running = True
    solve_time = None
    start = time.time()

    while running and T > 0.001:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_cost == 0:
            solve_time = time.time() - start
            break

        new = neighbor(current)
        new_cost = cost_function(new)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new
            current_cost = new_cost

        T *= 0.99
        draw_board(screen, current, size)
        pygame.time.delay(1)

    if solve_time is None:
        solve_time = time.time() - start

    print("Final state:", current)
    print("Final cost:", current_cost)
    print(f"Solve time: {solve_time:.4f}s")

    # keep window open until user closes it
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

    pygame.quit()

if __name__ == "__main__":
    n = int(input("Provide n (size of the board): "))
    state = create_state(n)
    print("Initial state:", state)
    print("Initial cost:", cost_function(state))
    run_visual(state)