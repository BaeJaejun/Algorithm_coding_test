import sys
input = sys.stdin.readline
    
n = int(input())
x = [0 for _ in range(100001)]

for _ in range(n):
    x[int(input())]+=1

for a in range(100001):
    if x[a] != 0:
        for _ in range(x[a]):
            print(a)
