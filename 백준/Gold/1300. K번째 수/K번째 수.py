import sys

input = sys.stdin.readline


N = int(input().strip())

k = int(input().strip())

low = 1
high = N*N
result = 0

def check(mid):
    cnt = 0
    
    for i in range(1,N+1):
        cnt += min(mid//i, N)  
    
    return cnt
    
while low <= high:
    mid = (low + high) // 2
    if check(mid) >= k:
        result = mid
        high = mid -1
    else:
        low = mid + 1
        
print(result)