import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    if dist[u][v] > w:
        dist[u][v] = w
    
for i in range(1,n+1):
    dist[i][i] = 0


def flo():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
                
flo()

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == float('inf'):
            print(0,end = " ")
        else:
            print(dist[i][j],end = " ")
    print()