import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recursion(start,sub,end,N):
    if N == 1:
        print(f'{start} {end}')
        return
    
    recursion(start,end,sub,(N-1))
    print(f'{start} {end}')
    recursion(sub,start,end,(N-1))
    
    

N = int(input().strip())

print(2**N - 1)
recursion(1,2,3,N)