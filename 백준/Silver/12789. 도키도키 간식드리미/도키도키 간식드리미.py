import sys

input = sys.stdin.readline

n = int(input().strip())

line = list(map(int,input().split()))

stk = [0]
cur = 1

for i in line:
    while(stk[-1] == cur):
        stk.pop()
        cur += 1
        
    if cur == i :
        cur += 1
        continue
    
    if cur < i:
        stk.append(i)

while(stk):
    if cur == stk[-1]:
        cur += 1
        stk.pop()
    else:
        break

    
if stk[-1] != 0:
    print("Sad")
else:
    print("Nice")