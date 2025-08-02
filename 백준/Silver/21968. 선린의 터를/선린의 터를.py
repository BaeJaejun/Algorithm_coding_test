import sys

input = sys.stdin.readline

t = int(input().strip())


for _ in range(t):
    n = int(input().strip())
    
    binary = bin(n)[2:][::-1]
    
    sumi = 0
    for i,k in enumerate(binary):
        if k == '1':
            sumi += int(k) * (3 ** i)
            
    
    print(sumi)
            
