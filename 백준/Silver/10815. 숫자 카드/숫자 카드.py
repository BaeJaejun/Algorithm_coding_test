import sys
input = sys.stdin.readline

n = int(input())
cardlist = {x: 1 for x in list((map(int,input().split())))}

m = int(input())
listx = list(map(int,input().split()))

ret = list()

for x in listx:
    if x in cardlist:
        print(1, end= " ")
    else:
        print(0,end= " ")