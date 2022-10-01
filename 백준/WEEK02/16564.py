from itertools import count
from logging import _Level
import sys

sys.stdin = open("input.txt","r")
charactor_num, max_level = map(int, sys.stdin.readline().split())
chractor_level = [int(sys.stdin.readline()) for i in range(charactor_num)]

