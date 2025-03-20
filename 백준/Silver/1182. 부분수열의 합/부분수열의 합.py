import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,S = map(int,input().split())

n_list = list(map(int,input().split()))
sum_list = []
sol_list = set()
#visited = [False] * N

def sol(s,idx):
    global cnt
    if s == sum(sum_list) and len(sum_list) > 0:
        #sol_list.add(tuple((sorted(sum_list[:]))))
        cnt += 1
        
    
    for i in range(idx, len(n_list)):
        #if visited[i] == False:
        sum_list.append(n_list[i])
        #   visited[i] = True
        sol(s,i+1)
        #  visited[i] = False
        sum_list.pop()


cnt = 0

sol(S,0) # 순열뽑기 조합으로 어떻게? 이차원배열에서 중복제거?
        # idx 현재 인덱스를 추가해서 다음 배열에서 배열 시작지점을 골라줌
print(cnt)
#print(sol_list)
#print(len(sol_list))