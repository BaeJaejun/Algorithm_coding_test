import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())

W =[]
for _ in range(N):
    W.append(list(map(int, input().split())))

N_list = [i for i in range(N)]

min_cost = float('inf')

for x in permutations(N_list): #순열 조합 하나에서 이동하는 경우 하나 뽑기
    cost = 0  
    visited = [False for _ in range(N)] # 이동 여부를 판별 N개 마을 이 있으면 N번 움직임
    
    for y in range(N): 
        c = W[ x[y%(N)] ][ x[(y+1)%N] ]
        if  c == 0:  
            break
        else:
            visited[x[y]] = True
            cost += c
                
    if False not in visited and min_cost > cost:
        min_cost = cost
    
    
print(min_cost)