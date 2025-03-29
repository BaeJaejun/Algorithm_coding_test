import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline
T = int(input().strip())


for _ in range(T):
    check = True
    V,E = map(int,input().split())
    
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (V+1)
    def dfs(start,color):
        global check
        visited[start] = color
        for i in graph[start]:
            if visited[start] == visited[i]:
                    check = False
                    return
            if visited[i] == -1: 
                dfs(i,(color + 1)%2)
        
    for i in range(1,V+1): #모든 정점에서 dfs 해서 분리된 그래프에서도 돌아가게
        if visited[i] == -1:
            dfs(i,0)
    
    if check:
        print("YES")
    else:
        print('NO')
    