import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

N = int(input().strip())

heap = []

for _ in range(N):
    x = int(input().strip())
    
    if x == 0:
        if heap:
            print(-1 * heappop(heap))
        else:
            print(0)
    else:
        heappush(heap,-x)