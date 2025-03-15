import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

#열의 끝까지 갔을 때 리턴 <-- 종료 조건
#재귀를 반복할수록 다음 열로 진행된다.
cnt = 0

def visit(start,N):
    global cnt 
    for i in range(N):    
       if not visited[i] and not diagonal1[i+start] and not diagonal2[i-start + N - 1]: # 행조건 대각조건1 대각조건2
            pos[start] = i            
            if start == N-1: #열의 끝까지 왔으면 cnt 올리고 7이 아니면 돌아가
                cnt += 1
            else:            
                visited[i] = diagonal1[i+start] = diagonal2[i-start + N-1] = True
                visit(start + 1,N)
                visited[i] = diagonal1[i+start] = diagonal2[i-start + N-1] = False  # 백트래킹 틀렸으니까 돌아가라
    return           
                

n = int(input())

pos = [0 for _ in range(n)] # 현재 열에서 위치가 어디인가
visited = [False for _ in range(n)] # 못가는 행 방문 처리리
diagonal1 = [False for i in range(2*n-1)] # 합 대각
diagonal2 = [False for i in range(2*n-1)] # 차 대각

visit(0,n)

print(cnt)