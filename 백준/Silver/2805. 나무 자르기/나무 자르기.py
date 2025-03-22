import sys
input = sys.stdin.readline

N, M = map(int,input().split())

trees = list(map(int,input().split()))

ground = 0
top = max(trees)

def check_sum(mid):
    total = sum((tree-mid) for tree in trees if tree > mid)
    return total

while ground <=  top:
   
    mid = (ground + top) // 2
    
    if check_sum(mid) >= M:
        ground = mid +1
    else:
        top = mid -1

print(top)