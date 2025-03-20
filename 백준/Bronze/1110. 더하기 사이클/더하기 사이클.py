import sys

input = sys.stdin.readline

N = int(input().strip())
cnt = 0
new_N = 0

def sol(N,start):
    global new_N
    global cnt
    
    if start == new_N:
        return 
    cnt +=1
        
    x = N % 10 + N // 10
    new_N = (N % 10) * 10 + x%10
    sol(new_N,start)
    
x = N * 10 if N < 10 else N
sol(x,x)
if x == 0:
    print(1)
else:
    print(cnt)