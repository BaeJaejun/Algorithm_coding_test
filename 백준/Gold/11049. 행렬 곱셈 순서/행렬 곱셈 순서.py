import sys

input = sys.stdin.read


data = list(map(int,input().split()))
n = data[0]
matrix = [(data[i],data[i+1]) for i in range(1,len(data),2)]

dp = [[0 if i==j else float('inf') for i in range(n)]for j in range(n)]

    
for length in range(1,n):
    for i in range(n - length):
        j = i + length
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1]))
            
print(dp[0][n-1])