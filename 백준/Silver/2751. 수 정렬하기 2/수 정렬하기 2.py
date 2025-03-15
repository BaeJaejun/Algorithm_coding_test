import sys
input = sys.stdin.readline
    
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))

for a in sorted(x):
    print(a)
