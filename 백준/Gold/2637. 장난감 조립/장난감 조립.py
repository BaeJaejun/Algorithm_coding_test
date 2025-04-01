import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
# ~1-N 중간부품 // N 완제품

indeg = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

# dfs (시간초과)
# for _ in range(M):
#     u,v,w = map(int,input().split())
#     graph[u].append((v,w))
#     indeg[v] += 1
      
# result = [0 for _ in range(N+1)]

# 완제품 -> 부품으로 개수를 셈셈
# def sol(N,cnt):
#     for i,k in enumerate(graph[N]):
#         if len(graph[k[0]]) == 0:
#             result[k[0]] += k[1] * cnt
#         else:
#             sol(k[0],k[1] * cnt)
        
# sol(N,1)

# for i,k in enumerate(result):
#     if k != 0:
#         print(f"{i} {k}")


# 화살표 작은수에서 큰수로

#그래프/indegree 만들기기
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[v].append((u,w))
    indeg[u] += 1


basic = [] #기본부품 알아내기
q = deque()
for i in range(1,N):
    if indeg[i] == 0:
        q.append(i)
        basic.append(i)

#기본부품의 개수 세기
#기본부품 -> 완제품으로 개수를 셈 (시간초과)
# def sol(N,c):
#     sum_cnt = 0
#     if len(graph[N]) == 0:
#         return c
#     for x in graph[N]:
#         cnt = x[1]
#         sum_cnt += sol(x[0],c * cnt)
#     return sum_cnt
        
#for i in sorted(basic):
#     print(f'{i} {sol2(i,1)}')

#갯수 기억을 위한 dp 테이블 ( 1~n 까지 여러가지의 개수가 필요하니까 n*n)
need = [[0 for _ in range(N+1)] for _ in range(N+1)]

#위상정렬과 동시에 need에 개수 업데이트
topo = []  
while q:
    idx = q.popleft()
    topo.append(idx)
    for i in graph[idx]:
        need[i[0]][idx] += i[1]
        if idx not in basic:
            for j,k in enumerate(need[idx]):
                if j != 0:
                    need[i[0]][j] += i[1] * k
        indeg[i[0]] -= 1
        if indeg[i[0]] == 0:
            q.append(i[0])


for i in sorted(basic):
     print(f'{i} {need[N][i]}')