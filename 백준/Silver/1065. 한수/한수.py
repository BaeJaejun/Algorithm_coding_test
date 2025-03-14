def hansu3(num):
    cnt = 0
    for i in range(100,num+1):
        if (int(str(i)[0]) - int(str(i)[1])) == (int(str(i)[1]) - int(str(i)[2])):
            cnt += 1
        
    return cnt


x = input()

if len(x) == 1:
    print(int(x))
elif len(x) == 2:
    print(int(x))
elif len(x) == 3:
    print(hansu3(int(x))+ 99)
else: 
    print(hansu3(999)+ 99)