import sys

input = sys.stdin.readline


def recursion(depth,n,m,current):
    if len(current) > 1  and (current[-1] - current[-2]) < 0:
                return
    if depth == m:
        print(' '.join(map(str,current)))
        return
    
    for i in range(n):
        if not visited[i]:
                      
            visited[i] = True
            recursion(depth+1,n,m,current + [a[i]])
            visited[i] = False    

N, M = map(int,input().split())
    
visited = [False] * N
a = [i for i in range(1,N+1)]
recursion(0,N,M,[])