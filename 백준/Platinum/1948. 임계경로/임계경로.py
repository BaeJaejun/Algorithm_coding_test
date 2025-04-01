import sys
from collections import deque
input = sys.stdin.readline


n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)] # 역방향 추적용
for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    reversed_graph[v].append((u,w))
    indeg[v] += 1    
start , end = map(int,input().split())


# 위상정렬해서 최장거리 찾기
q = deque()
q.append(start)
result = [start]
dist = [0 for _ in range(n+1)] 

while q :
    cur = q.popleft()
    for i,wei in graph[cur]:
        if dist[i] < dist[cur] + wei: # 최장거리 계산
            dist[i] = dist[cur] + wei 
        indeg[i] -= 1
        if indeg[i] == 0:
            q.append(i)
            result.append(i)


# 역추적해서 최장경로 찾아서 cnt 늘리기
visited = [False for _ in range(n+1)]
rq = deque()
rq.append(end)
visited[end] = True
count = 0

while rq:
    now = rq.popleft()
    for prev, weight in reversed_graph[now]:
        if dist[now] == dist[prev] + weight:
            count += 1
            if not visited[prev]:
                visited[prev] = True
                rq.append(prev)



print(dist[end])
print(count)