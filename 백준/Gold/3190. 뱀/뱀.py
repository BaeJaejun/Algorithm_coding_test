import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input().strip())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
K = int(input().strip())

for _ in range(K):
    x,y = map(int,input().split())
    board[x][y] = 1 #  사과 위치를 1로 표시시
L = int(input().strip())

direc = deque()

for _ in range(L):
    sec,di = input().split()
    direc.append([int(sec),di])

# 뱀 몸뚱이이
snake = deque([[1, 1]])

#    우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0
direc_idx = 0  #시작시엔 우측을 보고있다

def move(nowx,nowy): # 입력받는 좌표는 snake의 맨 오른쪽(대가리)
    global time,direc_idx
    
    time += 1
    movex = nowx + dx[direc_idx]
    movey = nowy + dy[direc_idx]
    if(movex > N or movex < 1 or movey > N or movey < 1): # 벽에 박았을 때
        return time
   
    if [movex,movey] in snake:
            return time
    
    snake.append([movex,movey])
    if board[movex][movey] == 1: #사과있음
        board[movex][movey] = 0
    else: #사과 없음
        snake.popleft()
    
    if direc and time == direc[0][0]:
        change_direc(direc[0][1])
        direc.popleft()
    return move(movex,movey)

def change_direc(t): # direc[i] 를 받아오자
    global direc_idx
    if t == "D":
        direc_idx = (direc_idx + 1) % 4
    elif t == "L":
        direc_idx = (direc_idx - 1) % 4

print(move(1,1))