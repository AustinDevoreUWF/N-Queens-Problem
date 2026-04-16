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
    #






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

#Needs the Creation of new States, take curr solution and checks near, but can also check outside

#Acceptance of the new State alg P(e,e-new, T)
# this requires, e= E(s)and the e-new= E(s-new)
# High t is more randomness, low T is more greedy

# T is determined by us as a var T= T * .90

#Main Algorithm Loop