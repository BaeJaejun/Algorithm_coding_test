import sys

input = sys.stdin.readline

n,m = map(int,input().split())

p = []

for _ in range(m):
    p.append(int(input().strip()))

p.sort(reverse=True)

max_result  = 0
max_price = 0
for i,price in enumerate(p):
    if i+1 <= n:
        if max_result < price * (i+1):
            max_result = price* (i+1)
            max_price = price
        if i+1 == n:
            break
    else:
        if max_result < price * n:
            max_result = price * n
            max_price = price
    
print(max_price, max_result)