import sys
from heapq import heappop,heappush
input = sys.stdin.readline

for _ in range(int(input().strip())):
    n = int(input().strip())
    rank = []
    for _ in range(n):
        
        rank.append(tuple(map(int,input().split())))
    
    rank.sort() 
    result = []
    cnt = 1  # 처음 1등인건 무조건 들어감
    heappush(result,(rank[0][1],rank[0][0]))
    
    for i in range(1,n):
        if rank[i][1] > result[0][0]:
            continue
        x, y = rank[i]
        heappush(result,(y,x))
    print(len(result))
    