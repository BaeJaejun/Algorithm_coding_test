import sys

input = sys.stdin.readline

w, l, d = map(float, input().split())

dp = [[0.0 for _ in range(4001)] for _ in range(21)]

dp[0][2000] = 1.0

for i in range(20):
    for score in range(1000,3001,50): # 50단위로 변하는 점수들
        if dp[i][score] > 0:
            # 여러 경로를 통해 확률이 증가될 수 있으니 += 사용
            if score + 50 <= 3000:
                dp[i+1][score + 50] += dp[i][score] * w
            dp[i+1][score] += dp[i][score] * d
            if score - 50 >= 1000:
                dp[i+1][score - 50] += dp[i][score] * l
            

print(f"{sum(dp[20][1000:1500]):.8f}")
print(f"{sum(dp[20][1500:2000]):.8f}")
print(f"{sum(dp[20][2000:2500]):.8f}")
print(f"{sum(dp[20][2500:3000]):.8f}")
print(f"{sum(dp[20][3000:3500]):.8f}")