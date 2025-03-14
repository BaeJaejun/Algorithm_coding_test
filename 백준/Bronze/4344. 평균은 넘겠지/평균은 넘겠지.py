import sys

input = sys.stdin.readline

C = int(input().rstrip())

for i in range(C):
    score = list(map(int,input().split()))
    
    avg = sum(score[1:]) / score[0]
    
    over_avg = 0
    for j in score[1:]:
        if j > avg:
            over_avg += 1
    
    print(f'{round((over_avg / score[0])*100,3):.3f}%')