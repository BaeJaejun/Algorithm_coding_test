import sys

input = sys.stdin.readline

N = int(input().strip())

paper  = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0
def check_num(x,y,N):
    sum = 0
    global white
    global blue
    for i in range(x,x+N):
        for j in range(y,y+N):
            sum += paper[i][j]
            
    if sum == 0:
        white += 1
    elif sum == N*N:
        blue += 1
    else:
        return False
    return True

def cut(x,y,N):
    if check_num(x,y,N): #내부에 숫자가 한종류면 
        return
    
    for i in range(x, x+N, N//2):
        for j in range(y,y+N, N//2):
            cut(i,j,N//2)
            
cut(0,0,N)

print(white)
print(blue)