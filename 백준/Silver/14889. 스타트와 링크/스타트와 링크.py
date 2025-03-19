import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().strip())

S = [list(map(int,input().split())) for _ in range(N)]

N_list = [i for i in range(1,N+1)]


N_com_list = list(combinations(N_list,N//2))  #절반은 1팀 절반은 2팀


overall1 = []
overall2 = []
min_overrall = float('inf')

#1팀
for a in N_com_list[:len(N_com_list)//2]: # 튜플갖고와서 튜플의 협력 오버롤을 더하자
    ovr_sum = 0
    for x in a:
        for y in a:
            if x != y:
                ovr_sum += S[x-1][y-1]
    overall1.append(ovr_sum)
#2팀
for a in N_com_list[-1:-(len(N_com_list)//2 + 1):-1]:
    ovr_sum = 0
    for x in a:
        for y in a:
            if x != y:
                ovr_sum += S[x-1][y-1]
    overall2.append(ovr_sum)

for x,y in zip(overall1,overall2):
    min_overrall = min(min_overrall,abs(x-y))
    
print(min_overrall)   
