import sys

input = sys.stdin.readline

board = [list(map(int,input().split()))for _ in range(9)] 

# def sol(i,j):
#     samsam(i,j)
#     garo(i,j)
#     sero(i,j)

# def garo(i,j):
#     n = [False] * 9 
#     zero = -1
#     if board[i].count(0) == 1:
#         for a,k in enumerate(board[i]):
#             if k != 0:
#                 n[k-1] = True 
#             else:
#                 zero = a
#         board[i][zero] = n.index(False)+1

# def sero(i,j):
#     n = [False] * 9 
#     zero_cnt = 0
#     zero = -1
#     for q in range(9):
#         if board[q][j] == 0:
#             zero_cnt += 1
            
#     if zero_cnt == 1:   
#         for a in range(9):
#             if board[a][j] != 0: 
#                 n[board[a][j]-1] = True 
#             else:
#                 zero = a   
#         board[zero][j] = n.index(False)+1
                
# def samsam(i,j):
#     I = i//3
#     J = j//3
#     n = [False] * 9
#     zero_cnt = 0
#     zerox = i
#     zeroy = j
#     for a in range(3):
#         for b in range(3):
#             if board[a + 3*I][b + 3*J] == 0:
#                 zero_cnt +=1
    
#     if zero_cnt == 1:
#         for a in range(3):
#             for b in range(3):
#                 if board[a + 3*I][b + 3*J] != 0:
#                     n[board[a + 3*I][b + 3*J] - 1] = True
            
#         board[zerox][zeroy] =  n.index(False)+1
def is_valid(x,y,num):
    for i in range(9):
        if board[x][i] == num:
            return False
    
    for i in range(9):
        if board[i][y] == num:
            return False
        
    sx, sy = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[sx + i][sy + j] == num:
                return False
    return True

empties = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def solve(idx):
    if idx == len(empties):
        return True
    x, y = empties[idx]
    for num in range(1, 10):
        if is_valid(x, y, num):
            board[x][y] = num
            if solve(idx + 1):
                return True
            board[x][y] = 0
    return False

solve(0)
for i in range(9):
    print( ' '.join(map(str,board[i])))