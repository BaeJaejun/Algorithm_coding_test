import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

normal = dict()
special = dict()
service = set()

for _ in range(a):
    x, y = input().split()
    
    normal[x] = int(y)

for _ in range(b):
    x, y = input().split()
    
    special[x] = int(y)

for _ in range(c):
    x = input().strip()
    
    service.add(x)
    
    
n = int(input().strip())

n_charge = 0
s_charge = 0
ser_cnt = 0
result = True
for _ in range(n):
    x = input().strip()
    
    if x in normal:
        n_charge += normal[x]

    if x in special:
        s_charge += special[x]
    
    if x in service:
        ser_cnt += 1
        
if ser_cnt > 1:
    result = False

if n_charge + s_charge < 50000 and ser_cnt > 0 :
    result = False
    
if n_charge < 20000 and s_charge > 0:
    result = False
    
if result:
    print("Okay")
else:
    print("No")    


