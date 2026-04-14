import random

# 1. Get size of board
# 2. state = 0->n for each placement
# 3. Shuffle 0->n

n = int(input("Provide n (size of the board): "))
def initial_state(n):
    state = list(range(n))
    random.shuffle(state)
    return state
result = initial_state(n)
print(result)
    #n is num of columns, row numbers are random nums 0-n

# Needs Initial State use a random generation

#COST-Function(Objective Function) goal is attacking queens is Q=0(no queens attacking)so lower is best
# So this is the main function for determination

#Needs the Creation of new States, take curr solution and checks near, but can also check outside

#Acceptance of the new State alg P(e,e-new, T)
# this requires, e= E(s)and the e-new= E(s-new)
# High t is more randomness, low T is more greedy

# T is determined by us as a var T= T * .90

#Main Algorithm Loop