from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited = [[False] * m for _ in range(n)]
    
    q = deque([(0,0,1)])
    visited[0][0] = True
        
    while q:
        a, b, cnt = q.popleft()
        if a == n - 1 and b == m - 1:
             return cnt
                
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny,cnt + 1))
        

    return -1