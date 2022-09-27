# 일곱 난장이
import sys
sys.stdin = open("input.txt","r")

snow_white = []

for i in range(9):
    snow_white.append(int(sys.stdin.readline()))

dobi = sum(snow_white) - 100

dobi_one = 0
dobi_two = 0

for i in range(len(snow_white)):
    for j in range(len(snow_white)):
        #
        if snow_white[i] + snow_white[j] == dobi:
            dobi_one = i
            dobi_two = j
            break

if dobi_one < dobi_one:
    snow_white.remove(snow_white[dobi_two])
    snow_white.remove(snow_white[dobi_one])
else :
    snow_white.remove(snow_white[dobi_one])
    snow_white.remove(snow_white[dobi_two])
    
new_snow = sorted(snow_white)
print(new_snow)