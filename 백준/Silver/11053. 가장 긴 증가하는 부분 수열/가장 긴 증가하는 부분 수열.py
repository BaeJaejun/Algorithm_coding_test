import sys
from bisect import bisect_left
input = sys.stdin.readline


N = int(input().strip())

A = list(map(int,input().split()))

def binary(arr, target):
    left = 0
    right = len(arr) - 1
    pos = len(arr)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            pos = mid
            right = mid -1
        else:
            left = mid + 1
    
    return pos

lis = []
for i in A:
    idx = binary(lis,i)
    if idx == len(lis):
        lis.append(i)
    
    else:
        lis[idx] = i
        

print(len(lis))
    
    