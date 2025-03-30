import sys

input = sys.stdin.readline

N,M = map(int,input().split())

graph_hi = [[] for _ in range(N+1)]
graph_lo = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph_hi[u].append(v)
    graph_lo[v].append(u)


mid = (N+1)//2

def dfs(visited,start,graph):
    visited[start] = True
    for x in graph[start]:
        if visited[x] == False:
            dfs(visited,x,graph)

result = 0

for i in range(1,N+1):
    visited_h = [False] * (N+1)
    visited_l = [False] * (N+1)
    dfs(visited_h,i,graph_hi)
    dfs(visited_l,i,graph_lo)
    
    if visited_h.count(True)-1 >= mid or visited_l.count(True)-1 >= mid:
        result += 1

print(result)
        