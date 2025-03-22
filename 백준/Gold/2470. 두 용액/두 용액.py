import sys

input = sys.stdin.readline

N = int(input().strip())

liquids = list(map(int,input().split()))
liquids.sort()

pl = 0
pr = len(liquids) - 1

zerozero = float('inf')

while pl < pr:
    sumL = liquids[pl] + liquids[pr]

    if abs(sumL) < abs(zerozero):
        zerozero = sumL
        x = pl
        y = pr
    if sumL < 0:
        pl += 1
    else:
        pr -= 1
        
print(liquids[x],liquids[y])