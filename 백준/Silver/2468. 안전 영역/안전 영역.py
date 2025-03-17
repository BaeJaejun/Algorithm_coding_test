import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())

area = [list(map(int, input().split())) for _ in range(N)]

max_h = max(map(max,area)) # 배열 내에 있는 최대 높이 < 이 밑으로 물높이 계산ㄱㄱ

# 우 좌 하 상 이동방향
dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

def safe(x,y):
    if flood[x][y] != -1:
        flood[x][y] = 3 # 3이 입력되면 방문처리
        i = 0
        for i in range(4):
            if 0 <= x+dx[i] < N  and 0 <= y+dy[i] < N and flood[x+dx[i]][y+dy[i]] == 0:
                safe(x + dx[i],y + dy[i])


# 0,0 에서 시작하고 물 높이 최대
sol = []
for water_h in range(max_h): #비가 오지 않는 경우부터 고려
    flood = [[0 for _ in range(N)] for _ in range(N)] # 잠길 위치 표시
    cnt = 0
    #잠기는 위치 계산
    for i in range(N):
        for j in range(N):
            if area[i][j] <= water_h:
                flood[i][j] = -1 # 물에 잠김
    
    #안전지대 계산하기 
    for i in range(N):
        for j in range(N):
            if flood[i][j] == 0:
                cnt += 1
                safe(i,j)
    sol.append(cnt)
            
print (max(sol))