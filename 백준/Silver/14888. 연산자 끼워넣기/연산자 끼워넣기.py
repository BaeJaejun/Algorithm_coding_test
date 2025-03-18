import sys

input = sys.stdin.readline

N = int(input().strip())

A = list(map(int,input().split()))

# + - * /
op = list(map(int,input().split()))
real_op = [] 


for i in range(4): # 연산자 4개임
    for j in range(op[i]):
        if i == 0:
            real_op.append('+')
        elif i == 1:
            real_op.append('-')
        elif i == 2:
            real_op.append('*')
        elif i == 3:
            real_op.append('/')

max_result = -float('inf')
min_result = float('inf')
op_list = []
visited = [False] * len(real_op)
def recursion(depth,op_len,current):
    if depth == op_len:
        op_list.append(current[:])
        #print(' '.join(map(str,current)))
        return 

    for i in range(op_len):
        if not visited[i]:
            visited[i] = True
            recursion(depth+1,op_len,current + [real_op[i]])
            visited[i] = False    
    
recursion(0,len(real_op),[])

#중복 연산자가 있을 때 생길 중복 순열을 제거

set_op_list = set(tuple(op) for op in op_list)

no_dup_op_list = list(list(op) for op in set_op_list)


for i in range(len(no_dup_op_list)):
    value = A[0]
    for a in range(len(A)-1):
        if no_dup_op_list[i][a] =="+":
            value +=  A[a+1]
        elif no_dup_op_list[i][a] =="-":
            value -= A[a+1]
        elif no_dup_op_list[i][a] =="*":
            value *= A[a+1]
        elif no_dup_op_list[i][a] =="/":
            if value < 0:
                value = -(-value // A[a+1])
            else:
                value = value // A[a+1]
    
    if max_result < value:
        max_result = value
    if min_result > value:
        min_result = value
        
        
print(max_result)
print(min_result)