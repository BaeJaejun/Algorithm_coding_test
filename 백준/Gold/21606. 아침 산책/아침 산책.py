import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input().strip())
A = [0]
A = A + list(map(int,input().strip()))

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
   
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]
total_cnt = 0

# 흰색 노드 체크
def dfs(i): # cnt == 흰색 주변 검은색 개수
    visited[i] = True
    black_cnt = 0
    # 흰색 주변에 최소 2개의 검은색이 있어야 cnt 가 올라감
    for x in graph[i]:
        if visited[x] == False:
            if A[x] == 1:
                black_cnt += 1         
            else:
                black_cnt += dfs(x)
          
    return black_cnt 
        
             
             
for i in range(1,n+1):
    if not visited[i] and A[i] == 0:
        for j in graph[i]:
            #다른 덩어리의 흰색 노드 주변을 false로 바꿔주기
            if visited[j] == True:
                visited[j] = False
        x = dfs(i)
        total_cnt += x * (x-1)
        

#검은색 노드 체크
for i in range(1, n + 1):
    if A[i] == 1:
        for j in graph[i]:
            if A[j] == 1:
                total_cnt += 1   
print(total_cnt)