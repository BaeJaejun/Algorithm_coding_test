import sys

input= sys.stdin.readline

def permutation(A,N,PA):
    A.sort()
    used = [False for _ in range(N)]
        
    def gen(chosen,used):
        if len(chosen) == N:
            PA.append(chosen[:])
            return 
        
        for i in range(N):
            if not used[i]:
                chosen.append(A[i])
                used[i] = True
                gen(chosen,used)
                used[i] = False
                chosen.pop()
                
    gen([],used)

N = int(input().strip())

A = list(map(int,input().split()))
PA = list()

# 배열 순열 하나 
permutation(A,N,PA)

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|  구하기
maxA = 0
for j in PA:
    sumA = 0
    for i in range(0,N-1):
        sumA += abs(j[i] - j[i+1])
    if sumA > maxA:
        maxA = sumA
#출력
print(maxA)