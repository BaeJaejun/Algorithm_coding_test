import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    heavy[a].append(b)  # a가 b보다 무거움
    light[b].append(a)  # b가 a보다 가벼움

def dfs(start, graph, visited):
    for nxt in graph[start]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, graph, visited)

ans = 0
mid = (N + 1) // 2  # 중앙 기준

for i in range(1, N+1):
    visited_h = [False] * (N+1)
    visited_l = [False] * (N+1)

    dfs(i, heavy, visited_h)
    dfs(i, light, visited_l)

    heavy_count = visited_h.count(True)
    light_count = visited_l.count(True)

    if heavy_count >= mid or light_count >= mid:
        ans += 1

print(ans)
