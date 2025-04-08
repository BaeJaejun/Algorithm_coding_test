import sys

input = sys.stdin.readline

N, K = map(int,input().split())

item = []
for _ in range(N):
    w,v = map(int,input().split())
    
    item.append((w,v))
    

dp = [0 for _ in range(K+1)]

# print(item)

for w,v in item:
    for i in range(K,w-1,-1):
   
        dp[i] = max(dp[i],dp[i-w] + v)
    #     print(dp,"!@")
    # print("---")
print(dp[K])


# # 이전 상태 복사 방식 / 이전상태의 dp테이블을 복사해서 그걸 참조해서 한번만
# for w, v in item:
#     old_dp = dp[:]  # 이전 상태 복사
#     for i in range(w, K + 1):  # 정방향 가능
#         dp[i] = max(dp[i], old_dp[i - w] + v)