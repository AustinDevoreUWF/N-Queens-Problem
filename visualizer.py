import random
import math
import time
import pygame
from core import create_state, cost_function, neighbor


def draw_board(screen, state, size, queen_img, scale):
    n = len(state)
    cell = size // n

    screen.fill((255, 255, 255))

    for row in range(n):
        for col in range(n):
            color = (240, 240, 240) if (row + col) % 2 == 0 else (100, 100, 100)
            pygame.draw.rect(screen, color, (col * cell, row * cell, cell, cell))

            if state[col] == row:
                x = col * cell + (cell - scale) // 2
                y = row * cell + (cell - scale) // 2
                screen.blit(queen_img, (x, y))

    pygame.display.flip()


def run_visual(state):
    pygame.init()

    size = 600
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Simulated Annealing N-Queens")

    n = len(state)
    cell = size // n

    scale = int(cell * 0.8)
    queen_img = pygame.image.load("queen.png").convert_alpha()
    queen_img = pygame.transform.smoothscale(queen_img, (scale, scale))

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

        draw_board(screen, current, size, queen_img, scale)
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