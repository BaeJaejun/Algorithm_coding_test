import sys

input = sys.stdin.readline

n = int(input().strip())

# 2중 for문 -> 시간초과
# #약수의 합 배열 저장해두기
# fx = [0 for _ in range(1000001)]
# fx[1] = 1
# for i in range(2,n+1):
#     for j in range(1,int(i**(1/2))+1):
#         if i % j == 0:
#             fx[i] += j
#             if j**2 != i:
#                 fx[i] += i//j
# print(sum(fx[:n+1]))

result = 0
for i in range(1,n+1):
    result += (n // i) * i

print(result)