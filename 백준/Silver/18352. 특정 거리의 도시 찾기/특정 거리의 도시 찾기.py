import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    
visited = [-1] * (N+1)

def bfs(start):
    visited[start] = 0
    q = deque([start])
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1
                
bfs(X)           

cnt = 0
for i,k in enumerate(visited):
    if k == K:
        cnt +=1
        print(i)

if cnt == 0:
    print(-1)