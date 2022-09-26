# 단어정렬
# 문제 : 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#       길이가 짧은것부터 // 길이가 같으면 사전 순으로 

import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())

word = []

for _ in range(N):
    word.append(sys.stdin.readline().strip())

sort_word = []

num = 0
for i in range(N):
    
    if len(word) == num: 
        sort_word.append(word)
    
    num = num + 1        