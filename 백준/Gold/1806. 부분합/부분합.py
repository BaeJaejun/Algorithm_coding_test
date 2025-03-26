import sys

n,s = map(int,input().split())

li = list(map(int,input().split()))
prefix_sum = [0 for _ in range(n+1)]


# 누적합 계산
for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + li[i]
        
# 완전탐색(시간 초과)
# a,b = 0,1
# min_len = float('inf')

# while a < n and b < n:
#     sums = sum(li[a:b+1])
#     if sums < s:
#         b += 1
#     elif sums >= s:
#         min_len = min(min_len,b - a+1)
#         a += 1
#         b = a+1
        
# print(min_len) 

a, b = 0,1
min_len = float('inf')

while a < n+1 and b < n+1:
    sums = prefix_sum[b] - prefix_sum[a]
    if sums < s:
        b+=1
    elif sums >= s:
        min_len = min(min_len,b-a)
        a += 1
  
# 유효한 부분합을 찾지 못한 경우
if min_len == float('inf'):
    print(0)  
else:
    print(min_len)