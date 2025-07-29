import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(str,input().split())))

result = set()

    # 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j,depth, str_number):
    if depth == 5:
        result.add(str_number)
        return
    for k in range(4):
        if 0 <= dx[k] + i < 5 and 0 <= dy[k] +j < 5:
            dfs(dx[k] + i,dy[k] +j,depth+1,str_number + board[dx[k]+i][dy[k]+j])


for i in range(5):
    for j in range(5):
        number = board[i][j]
        dfs(i,j, 0, number)
        
print(len(result))