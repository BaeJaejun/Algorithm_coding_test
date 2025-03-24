import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

N = int(input().strip())
left = [] # max힙 중간값이 루트인
right = [] # min힙


for _ in range(N):
    x = int(input().strip())
    
    if len(left) == len(right):
        heappush(left,-x)
    else:
        heappush(right,x)

    
    if right and -left[0] > right[0]:
        lr = -heappop(left)
        rr = -heappop(right)
        heappush(right, lr)
        heappush(left, rr)
        
    
    print(-left[0]) 