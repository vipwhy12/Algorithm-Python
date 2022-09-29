from asyncore import read
import sys

N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split('/n')))