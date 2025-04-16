import sys

input = sys.stdin.readline

N = int(input().strip())
E = int(input().strip())
song = [set() for _ in range(N+1)]

for i in range(E):
    data = list(map(int,input().split()))
    cnt, people = data[0], data[1:]
    if 1 in people:
        for p in people:
            song[p].add(i)
    else:
        # 해당 그룹의 모든 사람들의 노래 정보 공유
        shared = set()
        for p in people:
            shared |= song[p]
        for p in people:
            song[p] = shared.copy()
            song[p].add(i)

for i in range(1, N+1):
    if song[1].issubset(song[i]):
        print(i)