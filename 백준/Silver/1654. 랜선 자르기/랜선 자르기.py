import sys
input = sys.stdin.readline

K, N  = map(int,input().split())

lan = []
for _ in range(K):
    lan.append(int(input().strip()))
    

min_lan = 1  #랜선의 최소길이는 1
max_lan = max(lan)  #랜선의 최대 길이는 주어진 선들중에 가장 긴값 / 짧은거 버리고 긴 선만 쓸 수도 있으니까
max_length = 0

def check(length):
    global max_length
    cnt = 0
    for x in lan:
        cnt += x//length
    
        
    if cnt >= N:
        max_length = max(max_length,length)
        return True
    else:
        return False    

while min_lan <= max_lan:
  
    mid = (min_lan + max_lan) // 2
    
    if check(mid):
        min_lan = mid + 1
    else:
        max_lan = mid - 1
    
print(max_length)