import sys
input = sys.stdin.readline

a= []
for i in range(9):
    a.append(int(input().strip()))
maxA = max(a)
print(maxA)
print(a.index(maxA)+1)