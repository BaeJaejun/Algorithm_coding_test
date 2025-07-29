import sys

input = sys.stdin.readline

n = int(input().strip())

coin = list(map(int,input().split()))

m = max(coin)
result = 0

for i,k in enumerate(coin):
    if k < m:
        result += m - k
    if m == k:
        if i + 1 < len(coin):
            m = max(coin[i+1:])
            
print(result)