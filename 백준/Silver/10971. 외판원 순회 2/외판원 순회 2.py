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
    check = 0
    if x[0] != 0:
        continue  # 출발지 고정 // 순환이라 출발지를 고정해도 상관 없음
    for y in range(N):
        c = W[ x[y%(N)] ][ x[(y+1)%N] ]
        if  c == 0:  
            check = 1
            break
        else:
            cost += c
            if cost >= min_cost:
                check = 1
                break
                
    if check == 0 and min_cost > cost:
        min_cost = cost
    
    
print(min_cost)