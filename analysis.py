import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from core import simulated_annealing

# ── config ─────────────────────────────

N_VALUES = list(range(8, 30))
COOLING_RATES = [0.999, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60]

T_START = 100
TRIALS = 500
TIME_LIMIT = 0.5


# ── experiments ───────────────────────

def run_experiments():
    results = defaultdict(dict)

    total = len(N_VALUES) * len(COOLING_RATES) * TRIALS
    print(f"Running {total} trials...\n")

    for n in N_VALUES:
        for cooling in COOLING_RATES:

            times, successes, costs, steps_list = [], [], [], []

            for _ in range(TRIALS):
                steps, success, cost = simulated_annealing(
                    n, cooling, T_START, max_steps=1000
                )

                successes.append(success)
                costs.append(cost)
                steps_list.append(steps)

            results[n][cooling] = {
                "success": np.mean(successes),
                "cost": np.mean(costs),
                "steps": np.mean(steps_list),
            }

            print(
                f"N={n:2d} c={cooling:<6} "
                f"succ={np.mean(successes):.0%} "
                f"steps={np.mean(steps_list):.0f} "
                f"cost={np.mean(costs):.2f}"
            )

    return results


# ── scoring ───────────────────────────

def score(x):
    return x["success"]

def compute_optimal(results):
    optimal = {}

    print("\n── Optimal Cooling per N ──")

    for n in N_VALUES:
        best_c = max(COOLING_RATES, key=lambda c: score(results[n][c]))
        optimal[n] = best_c

        r = results[n][best_c]
        print(
            f"N={n:2d} best={best_c} "
            f"succ={r['success']:.0%} steps={r['steps']:.0f}"
        )

    return optimal


# ── plots ─────────────────────────────

def plot_results(results, optimal):

    success_grid = np.array([
        [results[n][c]["success"] for c in COOLING_RATES]
        for n in N_VALUES
    ])

    steps_grid = np.array([
        [results[n][c]["steps"] for c in COOLING_RATES]
        for n in N_VALUES
    ])

    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    ax[0].imshow(success_grid, aspect="auto", vmin=0, vmax=1)
    ax[0].set_title("Success Rate")

    ax[1].plot(N_VALUES, [optimal[n] for n in N_VALUES], marker="o")
    ax[1].set_title("Optimal Cooling")

    ax[2].plot(N_VALUES, steps_grid.mean(axis=1), marker="o")
    ax[2].set_title("Steps vs N")

    plt.tight_layout()
    plt.show()


# ── main ──────────────────────────────

if __name__ == "__main__":
    results = run_experiments()
    optimal = compute_optimal(results)
    plot_results(results, optimal)