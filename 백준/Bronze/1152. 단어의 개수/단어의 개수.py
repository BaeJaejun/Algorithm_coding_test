import sys

input = sys.stdin.readline

string = input().strip()

cnt = 1
if string == "":
    print(0)
else:
    for s in string:
        if s == ' ':
            cnt +=1
        

    print(cnt)