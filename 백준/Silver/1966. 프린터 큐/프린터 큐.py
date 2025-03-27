import sys
from collections import deque
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N,M = map(int,input().split())
    important = deque(map(int,input().split()))

    important[M] = -important[M]
    target = important[M]

    cnt = 0
    
    while True:
        x = max(map(abs,important))
        if  abs(x) == abs(important[0]):
            cnt += 1
            if important[0] == target:
                break
            important.popleft()

        else:
            important.append(important.popleft())
    print(cnt)
    