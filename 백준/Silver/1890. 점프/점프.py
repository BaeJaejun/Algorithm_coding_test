import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

board = [list(map(int,input().split())) for _ in range(n)]
   
    #우, 하
dy = [1, 0]
dx = [0, 1]


# bfs
# 메모리 초과
# q = deque()
# q.append((0,0))
# cnt = 0
# while q:
#     x,y = q.popleft()
#     for i in range(2):  
#         nx = x + (dx[i] * board[x][y])
#         ny = y + (dy[i] * board[x][y])
#         if nx == n-1 and ny == n-1:
#             cnt +=1
#             break
#         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0:
#             q.append((nx,ny))
#            
# print(cnt)



#dfs
#시간 초과
# dp = [[0 for _ in range(n)] for _ in range(n)]

# def dfs(x,y):
    
#     for i in range(2):  
#         nx = x + (dx[i] * board[x][y])
#         ny = y + (dy[i] * board[x][y])
#         if nx == n-1 and ny == n-1:
#             dp[nx][ny] += 1
#             return
#         if 0 <= nx < n and 0 <= ny < n and board[x][y] != 0:
#             dp[nx][ny] += 1
#             dfs(nx,ny)
        
# dfs(0,0)
# print(dp[n-1][n-1])


# 0,0 n-1,n-1 까지 거리는 맨하탄 거리와 같음 2N-2
# 안의 수의 합이 6이 되는지만 보면 되나? dp 테이블에 합을 저장?
# 결국 점프 뛰면서 체크해야하지 않나? 그럼 dfs도 똑같은거 아닌감
# 아닌가 보다

#바텀 업 방식
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            continue
        jump = board[i][j]
        if jump == 0:
            continue
        
        if i+ jump < n:
            dp[i+jump][j] += dp[i][j]
        if j+ jump < n:
            dp[i][j+jump] += dp[i][j]
            
print(dp[n-1][n-1])