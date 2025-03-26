import sys
input = sys.stdin.readline

N = int(input().strip())

matrix = [list(map(int,input().split())) for _ in range(N)]


cnt1 = 0 # -1
cnt2 = 0 # 0
cnt3 = 0 # 1

def sol(mat):
    global cnt1,cnt2,cnt3
    
    if mat[0][0] == -1:
        if 0 in [x for row in mat for x in row] or 1 in [x for row in mat for x in row]:
            pass
        else:
            cnt1 +=1
            return
    elif mat[0][0] == 0:
        if -1 in [x for row in mat for x in row] or 1 in [x for row in mat for x in row]:
            pass
        else:
            cnt2 +=1
            return
    elif mat[0][0] == 1:
        if 0 in [x for row in mat for x in row] or -1 in [x for row in mat for x in row]:
            pass
        else:
            cnt3 +=1
            return
            
    for i in range(0,len(mat),len(mat)//3):
        for j in range(0,len(mat),len(mat)//3):
            submat = [row[j:j+len(mat)//3] for row in mat[i:i+len(mat)//3]]
            sol(submat)
            
sol(matrix)
print(cnt1)
print(cnt2)
print(cnt3)
