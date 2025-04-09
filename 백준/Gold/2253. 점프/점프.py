# BFS 방식 -> 최초 도달 시 이미 최단거리임.

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())

small = set(int(input().strip()) for _ in range(m))

INF = float('inf')
visited = defaultdict(lambda : False)

def bfs():
    q = deque()
    q.append((1,0))
    visited[(1,0)] = True
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            now_stone,now_jump = q.popleft()
            if now_stone == n:
                return cnt
            for j in [now_jump-1,now_jump,now_jump+1]:
                next_stone = j + now_stone
                if j >= 1 and next_stone <= n and next_stone not in small and visited[next_stone,j] == False:
                    visited[(next_stone,j)] = True
                    q.append((next_stone,j))
        
        cnt += 1
    return -1

print(bfs())