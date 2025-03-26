import sys
input = sys.stdin.readline

MOD = 1000000007

# n과 k 입력 받기
n, k = map(int, input().split())

# 팩토리얼 계산: fact[i] = i! mod MOD
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD

# k!와 (n-k)!의 모듈러 역원 계산 (페르마의 소정리 이용)
inv_fact_k = pow(fact[k], MOD - 2, MOD)
inv_fact_nk = pow(fact[n - k], MOD - 2, MOD)

# 이항 계수 계산
answer = fact[n] * inv_fact_k % MOD * inv_fact_nk % MOD

print(answer)
