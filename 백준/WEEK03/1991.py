#트리순회 다시 

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = dict()

for i in range(n):
    tmp = input().split()
    tree[tmp[0]] = [tmp[1], tmp[2]]


def preorder(start):
    if start == '.':
        return
    print(f'{start}')
    inorder(tree[start][0])
    inorder(tree[start][1])

def inorder(start):
    if start == '.':
        return
    inorder(tree[start][0])
    print(f'{start}')
    inorder(tree[start][1])


def postorder(start):
    if start == '.':
        return
    inorder(tree[start][0])
    inorder(tree[start][1])
    print(f'{start}')
    
preorder('A')
print('\n')

inorder('A')
print('\n')

postorder('A')
print('\n')
