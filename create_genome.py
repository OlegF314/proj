import random, sys
sys.stdout = open("genom.evo", "w")
a = list(range(80))
random.shuffle(a)
print(*a)