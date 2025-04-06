import sys

input = sys.stdin.readline

n,k = map(int,input().split())

things = []
for _ in range(n):
    w,v = map(int,input().split())
    things.append((w,v))
    

# dp[i][w]: i번째 물건까지 고려했을 때, 무게 w일 때의 최대 가치
# 이전 물건(i-1) 기준으로,
# 안 넣으면: dp[i-1][w]
# 넣으면: dp[i-1][w - weight] + value
# 두 값 중 max()로 더 큰 걸 선택해서 갱신
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = things[i-1]
    for j in range(1,k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight] + value)
            
print(dp[n][k])