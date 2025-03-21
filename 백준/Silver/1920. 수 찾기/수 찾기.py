import sys

input = sys.stdin.readline

N = int(input().strip())

N_list = list(map(int,input().split()))

M  = int(input().strip())

M_list = list(map(int,input().split()))

N_list.sort()

def sol(find_num,start,end):
    if start > end:
        print(0)
        return
    mid = (start+end)//2
    
    if N_list[mid] == find_num:
        print(1)
        return    
    
    
    if find_num < N_list[mid]:
        return sol(find_num,start,mid-1)    
    else:
        return sol(find_num,mid + 1, end)
        

for m in M_list:
    sol(m,0,N-1)