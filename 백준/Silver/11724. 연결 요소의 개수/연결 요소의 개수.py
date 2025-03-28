import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (V+1)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)
    

cnt = 0
i = 1
for i in range(1,V+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)