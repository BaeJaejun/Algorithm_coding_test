import sys

input = sys.stdin.readline

N, B = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

def mat_mul(A,B, mod):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result

def power(A,B,mod):
    if B == 1: # 답에 모듈러 연산 수행하자
        return [[x % mod for x in row] for row in A] # %
        
    half = power(A, B //2 ,1000)
    if B % 2 == 1:
        return mat_mul(mat_mul(half, half, mod),A,mod)
    else:
        return mat_mul(half,half,mod)
        
        
result = power(A,B,1000)

for row in result:
    print(*row)