import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()

result = int(a) * int(b) * int(c)
x = [0 for _ in range(10)]

for i in str(result):
    for j in range(10):
        if int(i) == j:
            x[int(i)] += 1
            break
            
for i in x:
    print(i)