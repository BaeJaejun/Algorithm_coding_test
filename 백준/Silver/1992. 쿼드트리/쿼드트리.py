import sys

input = sys.stdin.readline

N = int(input().strip())

Quad  = [input().strip() for _ in range(N)]

def check_com(x,y,n):
    sum = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            sum += int(Quad[i][j])
    
      
    if sum == n*n:
        print(1,end="")
    elif sum == 0:
        print(0,end="")
    else:
        return False
    return True

def compress(x,y,N):

    if check_com(x,y,N): # 종료조건
        return    
    
    print('(',end="")

    for i in range(x,x+N,N//2):
        for j in range(y,y+N,N//2):
            compress(i,j,N//2)
    print(")",end="")


compress(0,0,N)
