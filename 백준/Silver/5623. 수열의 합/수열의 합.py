import sys

input = sys.stdin.readline

n = int(input().strip())

matrix = [list(map(int,input().split())) for _ in range(n)]

result = [0 for _ in range(n)]

sumx = 0
for i in range(n):
    for j in range(i+1,n):
        sumx += matrix[i][j]    

sumgaro = sum(matrix[0])

a = (sumgaro - sumx/(n-1))

if n > 2:
    result[0] = int(a // (n-2))
    
else:
    result[0] = 1

for i in range(1,n):
    result[i] = matrix[0][i] - result[0]
print(*result)