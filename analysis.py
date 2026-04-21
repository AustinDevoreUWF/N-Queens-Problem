import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from core import simulated_annealing, hill_climbing


# ── config ─────────────────────────────

N_VALUES = list(range(8, 30))
TRIALS = 100

SA_COOLING = 0.85
T_START = 100


# ── generic runner ─────────────────────

def run_algorithm(algorithm, n, trials, **kwargs):
    results = []

    for _ in range(trials):
        steps, success, cost = algorithm(n, **kwargs)
        results.append((steps, success, cost))

    steps = np.mean([r[0] for r in results])
    success = np.mean([r[1] for r in results])
    cost = np.mean([r[2] for r in results])

    return {
        "steps": steps,
        "success": success,
        "cost": cost
    }


# ── experiment ─────────────────────────

def run_experiments():
    results = defaultdict(dict)

    print("Running HC vs SA experiments...\n")

    for n in N_VALUES:

        hc = run_algorithm(hill_climbing, n, TRIALS)
        sa = run_algorithm(
            simulated_annealing,
            n,
            TRIALS,
            cooling=SA_COOLING,
            T_start=T_START
        )

        results[n]["HC"] = hc
        results[n]["SA"] = sa

        print(
            f"N={n} | "
            f"HC succ={hc['success']:.0%} steps={hc['steps']:.1f} | "
            f"SA succ={sa['success']:.0%} steps={sa['steps']:.1f}"
        )

    return results


# ── plots ──────────────────────────────

def plot_results(results):

    N = list(results.keys())

    hc_success = [results[n]["HC"]["success"] for n in N]
    sa_success = [results[n]["SA"]["success"] for n in N]

    hc_steps = [results[n]["HC"]["steps"] for n in N]
    sa_steps = [results[n]["SA"]["steps"] for n in N]

    plt.figure()
    plt.plot(N, hc_success, marker="o", label="Hill Climbing")
    plt.plot(N, sa_success, marker="o", label="Simulated Annealing")
    plt.title("Success Rate vs N")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(N, hc_steps, marker="o", label="Hill Climbing")
    plt.plot(N, sa_steps, marker="o", label="Simulated Annealing")
    plt.title("Steps vs N")
    plt.legend()
    plt.show()


# ── main ───────────────────────────────

if __name__ == "__main__":
    results = run_experiments()
    plot_results(results)