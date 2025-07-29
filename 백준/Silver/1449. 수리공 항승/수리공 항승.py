import sys

input = sys.stdin.readline

n, l = map(int,input().split())

water = list(map(int,input().split()))
water = sorted(water)

interval = []
for i in range(n-1):
    interval.append(water[i+1] - water[i])

s = 0
cnt = 0
for i in interval:
    s += i
    if s + 1 > l:
        s = 0
        cnt += 1
    
print(cnt + 1)