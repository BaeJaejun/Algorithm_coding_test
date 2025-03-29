import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indeg = [0] * (N+1)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    indeg[v] += 1

q = deque()

for i in range(1,N+1):
    if indeg[i] == 0:
        q.append(i)

result = []
    
while q:
    now = q.popleft()
    result.append(now)
    for next in graph[now]:
        indeg[next] -= 1
        if indeg[next] == 0:
            q.append(next)
            
                
print(* result)   