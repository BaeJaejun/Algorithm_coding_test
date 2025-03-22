import sys

input = sys.stdin.readline

K = int(input().strip())

stk = []
for _ in range(K):
    x = int(input().strip())
    
    if x == 0:
        stk.pop()
    else:
        stk.append(x)
    
print(sum(stk))