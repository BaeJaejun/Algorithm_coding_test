import sys

input = sys.stdin.readline

paren = input().strip()

def is_right(paren):
    stk = []
    for x in paren:
        if not stk: 
            if (x == '[' or x == '('):
                stk.append(x)
            else:
                return False
        else:
            if x == "(" or x == "[":
                stk.append(x)
            elif x == ")" and stk[-1] == '(':
                stk.pop()
            elif x == "]" and stk[-1] == '[':
                stk.pop()
            else:
                return False
    
    if not stk:
        return True
    else:
        return False

def score(paren):
    score = 0
    stk = []
    for k in paren:
        if k == "(":
            stk.append(k)
        elif k == "[":
            stk.append(k)
            
        elif k == ")":
            temp = 0
            while stk:
                x = stk.pop()
                if x == "(":
                    stk.append(2 if temp == 0 else 2 * temp)
                    break
                elif isinstance(x,int):
                    temp += x
                
                
        elif k == "]":
            temp = 0
            while stk:
                x = stk.pop()
                if x == "[":
                    stk.append(3 if temp == 0 else 3 * temp)
                    break
                elif isinstance(x,int):
                    temp += x
        
    score = sum(stk)
    return score
    
if is_right(paren):
    print(score(paren))
else:
    print(0)