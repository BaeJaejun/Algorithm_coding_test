import sys
from collections import deque
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    
    graph[u].append((w,v))

start, end = map(int,input().split())

def dijk(start):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    q = [(0,start)]
    
    while q:
        wei, now = heappop(q) # pop된 노드는 이미 최단거리임이 증명된 노드
        
         # 지금 꺼낸 거보다 더 짧게 도달한 적 있다면 무시 및 힙에 남아있는 친구들도 정리된다.
        if wei > dist[now] : 
            continue
        
        # 넣는 다면 조기 종료 가능
        # if now == end:
        #     break 
        
        for cost,neighbor in graph[now]:
            new_dist = cost + wei
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(q,(new_dist,neighbor))
    
    return dist

result = dijk(start)
print(result[end])
                