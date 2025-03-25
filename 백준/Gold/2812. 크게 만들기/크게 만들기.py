import sys

input = sys.stdin.readline

N,K = map(int,input().split())

number = input().strip()

stk = []
cnt = 0
for i in number:
    while cnt < K and stk and int(i) > int(stk[-1]):
        stk.pop()
        cnt += 1
        
    
    stk.append(i)
print(int(''.join(stk[:N-K])))