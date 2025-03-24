import sys
from heapq import heappop, heappush,heapify
input = sys.stdin.readline

N = int(input().strip())

home_office = []
for _ in range(N):
    x,y = map(int,input().split())
    home_office.append(sorted([x,y])) # 작은값 큰값 / 집과 사무실
    
d = int(input().strip())
home_office.sort(key = lambda x : x[1])  #end 기준 정렬 why?

#완전 탐색(시간 초과)
# home_office.sort()

# max_human = 0
# for i in range(N):
#     cnt = 0
#     for j in range(N):
#         if home_office[i][0] <= home_office[j][0] <= home_office[i][0] + d and home_office[i][0] <= home_office[j][1] <= home_office[i][0] + d:
#             cnt += 1
#     max_human = max(max_human, cnt)
# print(max_human)

max_cnt = 0
heap = []
for start,end in home_office:
    if end - start > d:
        continue
    
    left = end - d
    heappush(heap,start)

    while heap and heap[0] < left:
        heappop(heap)
    
    max_cnt = max(max_cnt,len(heap))
    
print(max_cnt)