# 로또
import imp
from itertools import permutations



import sys

rotto = []

for i in range(10000):
    rotto.append(list(map(int, sys.stdin.readlines().split())))
    if rotto[i][0] == 0:
        break



for i in range():
    
    print(permutations(rotto))


