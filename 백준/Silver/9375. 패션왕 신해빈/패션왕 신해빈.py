import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    cloths = defaultdict(list)
    n = int(input().strip())
    for _ in range(n):
        cloth, types = input().split()
        cloths[types].append(cloth)
        
    ret = 1
    for i in cloths:
        ret *= (len(cloths[i]) + 1)
            
    print(ret -1)
        
        