import sys

input = sys.stdin.readline

n = int(input().strip())

result = []
for _ in range(n):
    line = input().strip()
    nu = ""
    for i in line:
        if i.isdigit():
            nu += i
        else:
            if len(nu) >= 1:
                result.append(int(nu))
                nu = ""
    if len(nu) >= 1:
        result.append(int(nu))

result.sort()

for i in result:
    print(i)