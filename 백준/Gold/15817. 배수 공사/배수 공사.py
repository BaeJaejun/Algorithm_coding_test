import sys

input = sys.stdin.readline

n, x = map(int,input().split())
l = []
c = []
for _ in range(n):
    a, b = map(int,input().split())
    l.append(a)
    c.append(b)
    
dp = [0] * (x + 1)
dp[0] = 1

for j in range(n):
    for i in range(x, -1, -1):
        if dp[i] == 0: continue
        for k in range(1, c[j]+1):
            if i + l[j] * k <= x:
                dp[i + l[j] * k] += dp[i]
            else:
                break
            
print(dp[x])