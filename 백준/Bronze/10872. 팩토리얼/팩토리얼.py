import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def fac(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * fac(n-1)

n = int(input().strip())

print(fac(n))