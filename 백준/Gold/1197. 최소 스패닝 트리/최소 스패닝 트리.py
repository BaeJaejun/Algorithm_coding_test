import sys
from heapq import heappush,heappop,heapify
input = sys.stdin.readline

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    u, v, weight = map(int,input().split())
    graph[u].append((weight,v))
    graph[v].append((weight,u))
    
def prim(start):
    visited[start] = True
    heap = graph[start] #선택 노드에서 최소힙으로 최소가중치를 갖는 간선 선택
    heapify(heap)
    res = 0
    
    while heap:
        weight, w = heappop(heap)
        if not visited[w]:  
            visited[w] = True
            res += weight
            for e in graph[w]:
                if visited[e[1]] == False:
                    heappush(heap, e)
            
    return res


print(prim(1))
