import sys

input = sys.stdin.readline

n = int(input().strip())

meetings = []
for _ in range(n):
    x, y = map(int,input().split())
    meetings.append((x,y))

meetings.sort(key= lambda x : (x[1], x[0]))    

result = []
end_time = 0
for i,j in meetings:
    if end_time <= i: 
        result.append((i,j))
        end_time = j
        
print(len(result))