import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    r, s = map(str,input().split())
    
    for i in s:
        print(i * int(r),end='')
    
    print()