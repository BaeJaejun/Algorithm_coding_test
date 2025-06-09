import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a = [] # 기존 리스트
a.append([0 for _ in range(m+2)])
for _ in range(n):
    a.append([0] + list(map(int,input().split())) + [0])
a.append([0 for _ in range(m+2)])  

    
# 1차 시도   
#print(2 * ( n * m + (max(a[1]) + max(a[2]) + max(a[3])) + (max(b[1]) + max(b[2]) + max(b[3]))))

# 겉넓이를 구하려면  4 3 4 일때 중간 2를 빼먹음 -> 앞 뒤 수의 차를 이용해서 구해보자

# 천장 + 바닥
result = 2 * n * m

# 좌/우 면 (각 행마다 인접 열 차이)
for i in range(n + 2):
    for j in range(1, m + 2):
        result += abs(a[i][j] - a[i][j-1])

# 앞/뒤 면 (각 열마다 인접 행 차이)
for i in range(n + 2):
    for j in range(1, m + 2):
        result += abs(a[i][j] - a[i-1][j])
        
print(result)            