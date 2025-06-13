import sys

input = sys.stdin.readline

n = int(input().strip())

ni = input().strip()

result = 0
for i in ni:
    result += int(i)
    
print(result)