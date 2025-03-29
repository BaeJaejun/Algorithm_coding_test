import sys

input = sys.stdin.readline

N = int(input().strip())

A = list(map(int,input().split()))

x = ['+', '-', '*', '/']
op1 = list(map(int,input().split()))
max_result = -float('inf')
min_result = float('inf')

op = []
for i in range(4):
    op += [x[i]] * op1[i]


result = []
visited = [False] * len(op)
def per(depth, n, current):
    if depth == n:
        result.append(current[:])
        return
    
    prev = None
    for i in range(n):
        if not visited[i] and op[i] != prev:
            visited[i] = True
            per(depth+1, n,current + [op[i]])
            visited[i] = False
            prev = op[i]

op.sort()
per(0,len(op),[])

for i in range(len(result)):
    value = A[0]
    for a in range(len(op)):
        if result[i][a] == '+':
            value += A[a+1]
        elif result[i][a] == '-':
            value -= A[a+1]
        elif result[i][a] == '*':
            value *= A[a+1]
        elif result[i][a] == '/':
            if value < 0:
                value = -1*((value * -1) // A[a+1])
            else:
                value = value // A[a+1]
        
    if max_result < value:
        max_result = value
    if min_result > value:
        min_result = value
        
        
print(max_result)
print(min_result)