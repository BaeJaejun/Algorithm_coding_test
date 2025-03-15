import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

cnt = 0 #이동횟수
def recur(N,r,c):
    global cnt
    if N == 1: 
        if r == 0 and c == 0:
            cnt += 0
        elif r == 0 and c == 1:
            cnt += 1
        elif r == 1 and c == 0:
            cnt += 2
        elif r == 1 and c == 1:
            cnt += 3
    else:
        if r < 2**(N-1) and c >= 2**(N-1): #1사분면
            cnt += 2**((2*N)-2)  
            
        elif r < 2**(N-1) and c < 2**(N-1): #2사분면
            cnt += 0
            
        elif r >= 2**(N-1) and c < 2**(N-1): #3사분면
            cnt += 2**((2*N)-1) 
            
        elif r >= 2**(N-1) and c >= 2**(N-1): #4사분면
            cnt += 2**(2*N-2) * 3 
            
        recur(N-1,r%(2**(N-1)),c%(2**(N-1)))
    


N,r,c = map(int,input().split())

recur(N,r,c)

print(cnt)