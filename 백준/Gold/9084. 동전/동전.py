import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    coin = list(map(int,input().split()))
    M = int(input().strip())
    
    coin_list = [0 for _ in range(M+1)]
    coin_list[0] = 1
    
    for x in coin:
        for i in range(x,M+1):
            coin_list[i] += coin_list[i-x]    
    print(coin_list[M])
    