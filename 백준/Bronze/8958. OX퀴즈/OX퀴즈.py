import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

T = int(input().rstrip())

for i in range(T):
    score = 0
    up_score = 0
    A = input().rstrip()
    for a in A:
        if a == 'O':
            up_score += 1
            score += up_score
        else:
            up_score = 0
    
    print(score)