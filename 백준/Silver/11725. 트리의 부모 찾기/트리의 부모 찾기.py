import sys
from collections import deque
V = int(input().strip())

graph = [[] for _ in range(V+1)]

for _ in range(V-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
parents = [0 for _ in range(V+1)]
visited = [False for _ in range(V+1)]

def bfs(x):
    visited[x] = True
    q = deque([x])
    while q:
        z = q.popleft()
        for i in graph[z]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                parents[i] = z
    


bfs(1)
for i in parents[2:]:
    print(i)
    