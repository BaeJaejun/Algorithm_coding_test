import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().strip())

liquid = list(map(int,input().split()))

liquid.sort()

# 완전 탐색 O(n^2) -> 느림
# result = float('inf')
# x,y = 0,0
# for i in range(N-1):
#     for j in range(i+1,N):
#         sumL = liquid[i] + liquid[j]
           
#         if result > abs(sumL):
#             x,y = i,j
#             result = abs(sumL)
# print(f'{liquid[x]} {liquid[y]}',end="")

# 이분탐색

zerozero = float('inf')
x,y = 0,0
for i in range(N):
    #값 한개 고정
    a = liquid[i]
    #값에 역수에 가장 가까운 값을 나머지배열에서 이진탐색으로 찾기
    target = -a
    
    left = i+1
    right = N-1
    while left <= right:
        mid = (left + right)//2
        b = liquid[mid]
        sumL = a + b
        
        if abs(sumL) < abs(zerozero):
            zerozero = sumL
            x,y = a, b    
        
        if sumL < 0 :
            left = mid + 1
        else:
            right = mid - 1
            

print(x, y)