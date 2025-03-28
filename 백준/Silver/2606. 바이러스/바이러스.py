import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V = int(input().strip())
E = int(input().strip())

visited = [False] * (V+1)
def dfs(one):
    visited[one] = True
    
    for i in com[one]:
        if visited[i] == False:
            dfs(i)
    
com = [[] for _ in range(V+1)]

for _ in range(E):
    u,v = map(int,input().split())
    com[u].append(v)
    com[v].append(u)
    
dfs(1)
cnt = -1
for i in visited:
    if i == True:
        cnt +=1
print(cnt)