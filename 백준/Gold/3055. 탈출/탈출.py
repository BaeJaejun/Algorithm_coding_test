import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

maps = []
for _ in range(R):
    x = input().strip()
    maps.append(list(x))
    
# S -> D 로 탈출  
# * 물, X 돌
# 매 분마다 물 채우고 비버 이동
#*에 대해서 큐에 넣고 maps 변화 우 s 이동 체크 후 다음 시간으로
# 도착할 수 없으면 KAKTUS 출력
#    상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[-1 for _ in range(C)] for _ in range(R)]
def bfs(startx,starty,water):
    #물 위치 넣기
    wq = deque(water)
    
    visited[startx][starty] = 0
    q = deque()
    #고슴도치 시작 위치 넣기
    q.append((startx,starty))
    
    while q:
        # 물 확장 먼저 다 끝내고 
        for _ in range(len(wq)):
            wx,wy = wq.popleft()
            for i in range(4):
                nwx = wx + dx[i]
                nwy = wy + dy[i]
             
                if 0 <= nwx < R and 0 <= nwy < C and visited[nwx][nwy] ==  -1 and maps[nwx][nwy] == '.':
                    maps[nwx][nwy] = "*"
                    wq.append((nwx,nwy))
                    
        # 고슴도치의 이동(BFS상 고슴도치는 여러마리 처럼 움직이니까 ) 
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == -1 and maps[nx][ny] in ('.' , 'D'):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    


waterxy = []   
for i in range(R):
    for j in range(C):
        if maps[i][j] == "*":
            waterxy.append((i,j))
        elif maps[i][j] == 'S':
            gosumdochi = (i,j)
        elif maps[i][j] == 'D':
            destination = (i,j)
            
bfs(gosumdochi[0],gosumdochi[1],waterxy)


if visited[destination[0]][destination[1]] < 0:
    print("KAKTUS")
else:
    print(visited[destination[0]][destination[1]])