import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    stk = []
    vps = input().strip()
    
    for i in vps:
        if i =='(':
            stk.append(i)
        else: # )
            if stk:
                stk.pop()
            else:
                stk.append(i)
                break
            
    if len(stk) >= 1:
        print("NO")
    else:
        print("YES")
    
    
    
    