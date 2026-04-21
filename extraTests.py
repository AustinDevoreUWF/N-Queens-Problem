import matplotlib.pyplot as plt
from analysis import run_algorithm, TRIALS, T_START
from core import simulated_annealing


def cooling_rate_experiment():
    cooling_rates = [0.70, 0.80, 0.85, 0.90, 0.95, 0.99]
    fixed_n = 20

    success_rates = []
    avg_steps = []
    avg_costs = []

    print(f"\nCooling-rate experiment for N={fixed_n}\n")

    for cooling in cooling_rates:
        sa = run_algorithm(
            simulated_annealing,
            fixed_n,
            TRIALS,
            cooling=cooling,
            T_start=T_START
        )

        success_rates.append(sa["success"])
        avg_steps.append(sa["steps"])
        avg_costs.append(sa["cost"])

        print(
            f"Cooling={cooling:.2f} | "
            f"Success={sa['success']:.0%} | "
            f"Steps={sa['steps']:.1f} | "
            f"Cost={sa['cost']:.2f}"
        )

    plt.figure()
    plt.plot(cooling_rates, success_rates, marker="o")
    plt.title(f"SA Success Rate vs Cooling Rate (N={fixed_n})")
    plt.xlabel("Cooling Rate")
    plt.ylabel("Success Rate")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(cooling_rates, avg_steps, marker="o")
    plt.title(f"SA Steps vs Cooling Rate (N={fixed_n})")
    plt.xlabel("Cooling Rate")
    plt.ylabel("Average Steps")
    plt.grid(True)
    plt.show()

    plt.figure()
    plt.plot(cooling_rates, avg_costs, marker="o")
    plt.title(f"SA Final Cost vs Cooling Rate (N={fixed_n})")
    plt.xlabel("Cooling Rate")
    plt.ylabel("Average Final Cost")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    cooling_rate_experiment()