import sys
import math

A, B = map(int, sys.stdin.readline().rstrip().split())

print(math.lcm(A, B))
