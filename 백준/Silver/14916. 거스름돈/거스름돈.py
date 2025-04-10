import sys

input = sys.stdin.readline

n = int(input().strip())

coins = [5,2]

cnt = 0

dp = []

cnt += n//coins[0]
gus = n % coins[0]

if gus % 2 == 1 and n > 5:
    gus += coins[0]
    cnt -= 1

cnt += gus//coins[1]
gus = gus % coins[1]

if gus != 0:
    print(-1)
else:
    print(cnt)  