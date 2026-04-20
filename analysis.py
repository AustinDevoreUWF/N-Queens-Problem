import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from core import simulated_annealing

# ── experiment config ──────────────────────────────────────────────────────────

N_VALUES      = list(range(4, 31))
COOLING_RATES = [0.999,0.90,.85,.80,.75,.65]
T_START       = 100
TRIALS        = 100

# ── run experiments ────────────────────────────────────────────────────────────

results = defaultdict(dict)
total = len(N_VALUES) * len(COOLING_RATES) * TRIALS

print(f"Running {total} total trials...\n")

for n in N_VALUES:
    budget = n ** 2 * 10        # tighten this number to stress test
    for cooling in COOLING_RATES:
        times, solved = [], []
        for _ in range(TRIALS):
            elapsed, success = simulated_annealing(n, cooling, T_START, max_steps=budget)
            times.append(elapsed)
            solved.append(success)
        success_rate = sum(solved) / TRIALS
        avg_time     = sum(times)  / TRIALS
        results[n][cooling] = (success_rate, avg_time)
        print(f"  N={n:2d}  budget={budget:7d}  cooling={cooling}  success={success_rate:.0%}  avg_time={avg_time:.3f}s")

# ── find optimal cooling rate per N ───────────────────────────────────────────

print("\n── Optimal Cooling Rate per N (best success within fixed budget) ──")
optimal_cooling = {}
for n in N_VALUES:
    best_rate = max(results[n][c][0] for c in COOLING_RATES)
    best_c = min(c for c in COOLING_RATES if results[n][c][0] == best_rate)
    optimal_cooling[n] = best_c
    rate, avg = results[n][best_c]
    print(f"  N={n:2d}  best cooling={best_c}  success={rate:.0%}  avg_time={avg:.3f}s")

# ── plots ──────────────────────────────────────────────────────────────────────

success_grid = np.array([
    [results[n][c][0] for c in COOLING_RATES]
    for n in N_VALUES
])

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# heatmap
im = axes[0].imshow(success_grid, aspect="auto", cmap="RdYlGn", vmin=0, vmax=1)
axes[0].set_xticks(range(len(COOLING_RATES)))
axes[0].set_xticklabels(COOLING_RATES, rotation=45)
axes[0].set_yticks(range(len(N_VALUES)))
axes[0].set_yticklabels(N_VALUES)
axes[0].set_xlabel("Cooling Rate")
axes[0].set_ylabel("Board Size N")
axes[0].set_title("Success Rate (fixed step budget)")
plt.colorbar(im, ax=axes[0])

# optimal cooling rate per N
axes[1].plot(N_VALUES, [optimal_cooling[n] for n in N_VALUES], marker="o", color="steelblue")
axes[1].set_xlabel("Board Size N")
axes[1].set_ylabel("Optimal Cooling Rate")
axes[1].set_title("Fastest Cooling Rate That Still Wins")
axes[1].grid(True)

# success rate curves per cooling rate
for c in COOLING_RATES:
    rates = [results[n][c][0] for n in N_VALUES]
    axes[2].plot(N_VALUES, rates, marker="o", label=f"c={c}")
axes[2].set_xlabel("Board Size N")
axes[2].set_ylabel("Success Rate")
axes[2].set_title("Success Rate vs N per Cooling Rate")
axes[2].legend(fontsize=7)
axes[2].grid(True)

plt.tight_layout()
plt.savefig("nqueens_cooling_analysis.png", dpi=150)
plt.show()
print("\nSaved to nqueens_cooling_analysis.png")