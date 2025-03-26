import sys

input = sys.stdin.readline

n = int(input().strip())
li = list(map(int,input().split()))
x = int(input().strip())

li.sort()

pl = 0
pr = len(li) - 1
cnt = 0
while pl < pr:
    if pl >= pr:
        break
    sum1 = li[pl] + li[pr]
    
    if sum1 == x:
        cnt +=1
        pl += 1
        pr -= 1
        
    elif sum1 > x:
        pr -= 1
        
    elif sum1 < x:
        pl += 1
        
print(cnt)