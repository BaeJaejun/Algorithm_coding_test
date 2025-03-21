import sys
input = sys.stdin.readline

N, C = map(int,input().split())
houses = []
for i in range(N):
    houses.append(int(input().strip()))
houses.sort()

min_dist = 1
max_dist = houses[-1] - houses[0]
result = 0

while min_dist <= max_dist:
    try_dist = (min_dist + max_dist) // 2
    last_installed = houses[0]
    count = 1

    for i in range(1, N):
        if houses[i] - last_installed >= try_dist:
            count += 1
            last_installed = houses[i]

    if count >= C:
        result = try_dist
        min_dist = try_dist + 1
    else:
        max_dist = try_dist - 1

print(result)
