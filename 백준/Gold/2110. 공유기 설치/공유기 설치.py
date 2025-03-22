import sys

input = sys.stdin.readline

N,C = map(int,input().split())

homes = []
for _ in range(N):
    homes.append(int(input().strip()))
    
homes.sort()

min_dist = 1
max_dist = homes[-1] - homes[0]

def check_C(mid):
    cnt = 1
    last_installed = homes[0]
    for x in homes[1:]:
        if x -last_installed >= mid:
            last_installed = x
            cnt += 1
    return cnt

while min_dist <= max_dist:
    interval = (min_dist + max_dist) // 2
    
    if check_C(interval) >= C:
        min_dist =  interval +1
    else:
        max_dist = interval -1
        
print(max_dist)