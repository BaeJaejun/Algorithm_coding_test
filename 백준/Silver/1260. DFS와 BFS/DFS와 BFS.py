import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[]  for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[v].append(u) 
    graph[u].append(v)

visited = [False] * (N+1)
def dfs(start):
    visited[start] = True
    print(start , end=' ')
    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(i)


visited2 = [False] * (N+1)

def bfs(start):
    visited2[start] = True
    q = deque([start])
    while q:
        x = q.popleft()    
        print(x,end= ' ')
        for i in sorted(graph[x]):
            if not visited2[i]:
                q.append(i)
                visited2[i] = True
    
    
dfs(V)
print()
bfs(V)