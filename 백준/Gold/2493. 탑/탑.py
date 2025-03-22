import sys

input = sys.stdin.readline

N = int(input().strip())
tower = list(map(int,input().split()))


#완전 탐색(시간초과)
# susin  =[0] * N
# for i in range(N-1,-1,-1):
#     for j in range(i-1,-1,-1):
#         if tower[i] < tower[j]:
#             susin[i] = j+1
#             break
        
# print(*susin)

susin = [0] * N
stk =[]
for i in range(N):
    
    while len(stk) > 0 and stk[-1][1] < tower[i]:
        stk.pop()
        
    if len(stk) > 0:
        susin[i] = stk[-1][0] + 1
    else:
        susin[i] = 0
    
    stk.append((i, tower[i]))
     
print(*susin)    
   