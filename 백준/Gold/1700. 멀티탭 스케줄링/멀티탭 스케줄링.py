import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

elec = deque(map(int,input().split()))

se = set()
cnt = 0

while elec:
    x = elec.popleft()
    
    if len(se) < n: #자리 있음 꽂아
        se.add(x)
        continue
    
    if x in se: # 이미 꽂혀있음 pass
        continue
    
    # 다 등장하면 마지막애 뽑고, 다 등장 안하며 안한애 뽑고
    check =  -1
    target = 0
    
    for plugged in se:
        if plugged in elec:
            idx = elec.index(plugged) 
        else:
            idx = float('inf') # 앞으로 안나옴
        
        if idx > check: # 더 먼 친구가 있으면 idx 갱신 
            check = idx
            target = plugged
    
    se.discard(target)
    cnt +=1
    se.add(x)
    
print(cnt)
