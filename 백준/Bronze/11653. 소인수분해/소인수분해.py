import sys

input = sys.stdin.readline

n = int(input().strip())

for i in range(2,10000000):
    if n == 1:
        break
    while(True):
        if n % i == 0:
            print(i)
            n = n // i
        else:
            break