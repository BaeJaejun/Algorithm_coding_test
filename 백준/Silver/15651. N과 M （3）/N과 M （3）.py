import sys

input = sys.stdin.readline

def permutaion(depth,n,m,current):
    if depth == m:
        print(" ".join(map(str,current)))
        return
    
    for i in range(n):
        permutaion(depth+1,n,m,current + [a[i]])
        
N,M = map(int,input().split())


a = [i for i in range(1,N+1)]

permutaion(0,N,M,[])