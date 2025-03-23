import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
que = deque()
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)