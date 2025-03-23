import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,k  = map(int,input().split())
deq = deque(i for i in range(1,n+1))

seq = list()
while len(deq) > 0:
    deq.rotate(-(k-1))
    seq.append(str(deq.popleft()))
    
print("<"+ ', '.join(seq)+">")
 