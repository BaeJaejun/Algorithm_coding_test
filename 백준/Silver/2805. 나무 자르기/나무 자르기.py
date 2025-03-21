import sys
input = sys.stdin.readline

N, M = map(int,input().split())

namu = list(map(int,input().split()))
    
    
def binary(start,end):
    if start > end:
        return end
        
    mid = (start + end) // 2
    
    total = sum((tree-mid) for tree in namu if tree > mid)
    
    if total >= M :
        return binary(mid + 1, end)
    else:
        return binary(start,mid - 1)

max_H = 0
namu.sort()

print(binary(0,max(namu)))

