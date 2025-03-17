import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recur(x,n):
    if n == 1:
        cantor[x] = '-'
        return
    
    DIVn = (n) // 3
    for i in range(3):
        if i == 1:
            continue
        recur(x + i*DIVn, DIVn)



while True:
    line = input()
    if not line:
        break
    
    n = int(line.strip())
    cantor = [' ' for _ in range(3**n)]
    recur(0,3**n)
    print(''.join(cantor))
    
    