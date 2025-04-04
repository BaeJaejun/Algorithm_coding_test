import sys

input = sys.stdin.readline

n = int(input().strip())

f_list = [0 for _ in range(n+2)]
f_list[1] = 1

for i in range(2,n+2):
    x = f_list[i-1] + f_list[i-2]
    f_list[i] = x
        
result = f_list[n]
print(result)