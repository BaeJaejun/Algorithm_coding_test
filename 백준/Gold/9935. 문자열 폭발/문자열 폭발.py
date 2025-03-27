import sys

input = sys.stdin.readline

first = input().strip()

bomb = input().strip()


# 시간초과
# while True:
#     if bomb in first:
#         for i in range(len(first)):
#             if first[i:i + len(bomb)] == bomb:
#                 first = first[:i] + first[i+len(bomb):]
           
#     else:
#         if len(first) == 0:
#             print('FRULA')
#         else:
#             print(first)
#         break
    
#스택
stk = []

for i in range(len(first)):    
    
    stk.append(first[i])
    if len(stk) >= len(bomb):
        x = "".join(stk[-len(bomb):])
        if  x== bomb:
            for _ in range(len(bomb)):
                stk.pop()
                
if len(stk) == 0:
            print('FRULA')
else:
            print("".join(stk))
