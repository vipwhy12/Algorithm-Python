# 일곱 난장이
from os import remove
import sys
sys.stdin = open("input.txt","r")
snow_white = []

for i in range(9):
    snow_white.append(int(sys.stdin.readline()))

dobi = sum(snow_white) - 100

one = 0
two = 0

for i in range(len(snow_white)):
    for j in range(len(snow_white)):
        if i != j:
            if snow_white[i] + snow_white[j] == dobi:
                one = i
                two = j
                break


if one > two: 
    snow_white.remove(snow_white[one])
    snow_white.remove(snow_white[two])
else:
    snow_white.remove(snow_white[two])
    snow_white.remove(snow_white[one])                

new_snow = sorted(snow_white)

for i in range(len(new_snow)):
    print(new_snow[i])