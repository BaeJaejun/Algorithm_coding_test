import sys
input = sys.stdin.readline

result = []
graph = [[] for _ in range(9)]
graph[1] = [4,5]
graph[2] = []
graph[3] = [4,5]
graph[4] = [2,3]
graph[5] = [8]
graph[6] = [2,3]
graph[7] = [8]
graph[8] = [6,7]

while True:
    x = input().strip()
    if x == "0":
        break

    valid = True

    if len(x) < 2 or x[0] != '1' or x[-1] != '2':
        valid = False
    else:
        for i in range(len(x) - 1):
            a = int(x[i])
            b = int(x[i+1])
            if a == 2:
                valid = False
                break
            if b not in graph[a]:
                valid = False
                break

    result.append("VALID" if valid else "NOT")

for i, k in enumerate(result):
    print(f"{i+1}. {k}")
