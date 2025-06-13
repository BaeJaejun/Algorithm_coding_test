import sys

input = sys.stdin.readline

n = int(input().strip())

word = input().strip()

result = 0

a = ""

for i in range(n):
    if word[i].isdigit():
        a += word[i]
    else:
        if a != "":
            result += int(a)
            a = ""
            
# 마지막이 숫자일때 처리
if a != "":
    result += int(a)        
        
print(result)