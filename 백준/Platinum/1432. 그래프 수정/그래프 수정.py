import sys
from collections import deque
input = sys.stdin.readline
from heapq import heapify, heappop, heappush
N = int(input().strip())

graph = [[-1 for _ in range(N+1)]]
outdegree = [0 for _ in range(N+1)]

for _ in range(N):
    seq = list(map(int,input().strip()))
    graph.append([-1] + seq)
    

# V1 -> V2  : V2 > V1

#역방향 그래프
reversed_graphlist =[[] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == 1:
            reversed_graphlist[j].append(i)
            outdegree[i] += 1
            

result = []
q = []
for i in range(1,N+1):
    if outdegree[i] == 0:
        heappush(q,-i)
        
while q:
    cur = -heappop(q)
    result.append(cur)
    for x in reversed_graphlist[cur]:
        outdegree[x] -= 1
        if outdegree[x] == 0:
            heappush(q,-x)


# 사이클 검사
if len(result) < N:
    print(-1)
else:
    ## 출력
    idx = [i for i in range(N,0,-1)]
    for k,i in sorted(zip(result,idx)):
        print(i,end=" ")
