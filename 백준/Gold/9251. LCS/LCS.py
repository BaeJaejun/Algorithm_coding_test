import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()

pA = len(A)
pB = len(B)

dp = [[0 for _ in range(pB+1)] for _ in range(pA+1)]

for i in range(1,pA+1):
    for j in range(1,pB +1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            

print(dp[pA][pB])