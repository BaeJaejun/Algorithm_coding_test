import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int,input().split()))

result = []

for i in range(N):
    if result:
        idx = bisect_left(result,A[i])
        if  idx == len(result):
            result.append(A[i])      
        else:
            result[idx] = A[i]
    else:
        result.append(A[i])
        

print(len(result))