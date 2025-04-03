import sys

input = sys.stdin.readline

N = int(input().strip())

map = []

for i in range(N):
    x = list(input().strip())
    map.append(x)
    

visited = [[False for _ in range(N)] for _ in range(N)]
    #상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(startx,starty,num,house_cnt):
    visited[startx][starty] = True
    for i in range(4):
        nx = startx + dx[i]
        ny = starty + dy[i]
        if 0<= nx < N and 0<= ny < N and visited[nx][ny] == False and map[nx][ny] == num:
           house_cnt = dfs(nx,ny,num,house_cnt) +1
    
    return house_cnt
       
    
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and map[i][j] != '0':
            h = dfs(i,j,map[i][j],1)
            result.append(h)
            cnt += 1
            
print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])