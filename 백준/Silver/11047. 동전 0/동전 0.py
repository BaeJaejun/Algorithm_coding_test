import sys

input = sys.stdin.readline

n,k = map(int,input().split())
A = []
for _ in range(n):
    A.append(int(input().strip()))
    

cnt = 0
for i in A[::-1]:
    if k == 0:
        break
    if k < i:
        continue
    else:
        cnt += k // i
        k = k % i
print(cnt)