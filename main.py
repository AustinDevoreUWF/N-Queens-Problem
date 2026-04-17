import random
import math
# Initial State
    # 1. Get size of board
    # 2. state = 0->n for each placement
    # 3. Shuffle 0->n
n = int(input("Provide n (size of the board): "))

def create_state(n):
    state = list(range(n))
    random.shuffle(state)
    return state
state = create_state(n)

print(state)
#Tempurature Figuring Algorithm
#COST-Function(Objective Function) goal is attacking queens is Q=0(0queens attacking)so lower is best
# So this is the main function for determination
def cost_function(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i+1,n):
            if(abs(state[i] - state[j]) == abs(i - j)):
                cost += 1
    return cost
cost = cost_function(state)
print(cost)

def neighbor(state):
    new = state.copy()
    i,j = random.sample(range(len(new)),2)
    new[i],new[j]  = new[j],new[i]
    return new

def simulated_annealing(state):
    current = state
    T = 100

    while T> .001:
        new = neighbor(current)
        delta = cost_function(new) - cost_function(current)

        if(delta<0):
            current = new
        else:#Set probability 
            P = math.exp(-delta / T)
            random.random()
#Needs the Creation of new States, take curr solution and checks near, but can also check outside