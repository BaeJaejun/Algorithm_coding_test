import sys

input = sys.stdin.readline

n = int(input().strip())

coinlist = [0 for _ in range(n+2)]

coinlist[1] = 1
coinlist[2] = 2

for i in range(3,n+1):
    coinlist[i] = (coinlist[i-1] + coinlist[i-2])%15746
    

print(coinlist[n])