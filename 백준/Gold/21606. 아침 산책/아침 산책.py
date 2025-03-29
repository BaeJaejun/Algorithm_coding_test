import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
A =[-1]
A = A + list(map(int,input().strip()))


graph = [[] for _ in range(N+1)]

for i in range(1,N):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
def dfs(start):
    global cnt
    visited[start] = True
    
    for i in graph[start]:
        if visited[i] == False:
            if A[i] == 1:
                cnt +=1
                continue
            else:
                dfs(i)

for j,k in enumerate(A):
    visited = [False] *(N+1)
    if k == -1:
        pass
    if k == 1:
        dfs(j)
        
print(cnt)