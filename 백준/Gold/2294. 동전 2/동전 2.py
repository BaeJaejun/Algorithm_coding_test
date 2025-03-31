import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

coin = set()

for _ in range(n):
    coin.add(int(input().strip()))

# 백트래킹 완전탐색(시간초과)
#coins = list(coin)
#coins.sort(reverse = True)

# min_cnt = float('inf')
# def sol(sums, cnt):
#     global min_cnt
    
#     #가지치기
#     if cnt >= min_cnt:
#         return
            
#     for i in coins:
#         ns = sums + i
#         nc = cnt + 1
#         if ns > k:
#             continue
#         elif ns == k:
#             min_cnt = min(min_cnt, nc)
#             continue
#         sol(ns, nc)
# sol(0,0)   
# print(min_cnt)


#금액 기준으로 생각을 하자
coins = list(coin)

#k까지의 금액을 배열로
dist = [-1] * (k+1)
dist[0] = 0
q = deque()
q.append(0)

while q:
    cur = q.popleft()
    
    for c in coins:
        nxt = cur + c
        if nxt > k:
            continue
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(dist[k])