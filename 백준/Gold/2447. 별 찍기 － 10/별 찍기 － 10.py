import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def recursion(x,y,N):
    if N == 3:
        for i in range(x,3+x):
            for j in range(y,3+y):
                if i == (1+x) and j == (1+y):
                    continue    
                stars[i][j] = '*'
    else:
        for i in range(x,x+N,N//3):
            for j in range(y,y+N,N//3):
                if i == x + N//3 and j == y + N//3:
                    continue
                recursion(i, j, N//3)
        
N = int(input().strip())
stars = [[' ' for _ in range(N)] for _ in range(N)]
recursion(0,0,N)

for i in range(N):
    for j in range(N):
        print(stars[i][j], end= '')
    print()

