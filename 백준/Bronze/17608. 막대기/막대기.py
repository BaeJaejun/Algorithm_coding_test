import sys

input = sys.stdin.readline

N = int(input().strip())
height = []
for _ in range(N):
    height.append(int(input().strip()))

cnt = 1
key = height[-1]

for _ in range(N):
    
    if height[-1] > key:
        cnt += 1
        key = height.pop()
    else:
        height.pop()
print(cnt)