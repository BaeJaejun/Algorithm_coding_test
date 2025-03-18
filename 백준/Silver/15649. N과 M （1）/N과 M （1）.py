import sys

input = sys.stdin.readline


def permutation(depth, n,m, current):
    if depth == m:
        print(' '.join(map(str, current)))
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            permutation(depth+1,n,m,current + [a[i]])
            visited[i] = False

N, M = map(int,input().split())

visited = [False for _ in range(N)]
a= []
for i in range(1,N+1):
    a.append(i)
    
permutation(0, N, M, [])
    
    