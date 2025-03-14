import sys

input = sys.stdin.readline


def hanoi(n,start,end):
    
    if n == 1 :
        print(f'{start} {end}')
        return
    
    hanoi(n-1,start,6-end- start)
    print(f'{start} {end}')
    hanoi(n-1,6-start-end, end)


n = int(input().strip())
print(2**n - 1)

if n <= 20:
    x = hanoi(n,1,3) 

    if x != None:
        print(x) 