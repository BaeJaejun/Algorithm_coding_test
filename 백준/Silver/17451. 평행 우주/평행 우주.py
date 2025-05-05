import sys, math

input = sys.stdin.readline

n = int(input().strip())

v = list(map(int,input().split()))

speed = v[-1]
for i in range(n-2, -1 ,-1):
    if v[i] > speed:
        speed = v[i]
    else:
        if speed % v[i]:
            speed = (speed//v[i] + 1) * v[i]
            
print(speed)
        