import sys

input = sys.stdin.readline

x, y = map(int,input().split())
n = int(input().strip())

garo = [0,y]
sero = [0,x]

for _ in range(n):
    A = list(map(int,input().split()))
    if A[0] == 0:
        garo.append(A[1])
    else:
        sero.append(A[1])

h = 0
w = 0
garo.sort()
sero.sort()
for i in range(1,len(garo)):
    m = garo[i]-garo[i-1]
    if m > h:
        h = m
        
for i in range(1,len(sero)):
    m = sero[i]-sero[i-1]
    if m > w:
        w = m

print(w * h)