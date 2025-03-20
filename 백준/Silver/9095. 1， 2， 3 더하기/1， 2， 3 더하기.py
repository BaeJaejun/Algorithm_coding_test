import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num = [1,2,3]

T = int(input().strip())
def sol(n,sumN):
    global cnt
    if sumN > n:
        return
    if sumN == n:
        cnt +=1
        return
    
    for i in num:
        sumN += i 
        sol(n,sumN)
        sumN -= i
        
for _ in range(T):
    cnt = 0
    n = int(input().strip())
    sol(n,0)
    print(cnt)
