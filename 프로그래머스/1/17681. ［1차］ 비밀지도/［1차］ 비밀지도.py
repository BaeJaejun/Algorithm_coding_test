def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    for i in arr1:
        a1.append(format(i,f'0{n}b'))
        
    for i in arr2:
        a2.append(format(i,f'0{n}b'))
        
    for i,j in zip(a1,a2):
        password = ''
        for x,y in zip(i,j):            
            if x == '0' and y == '0':
                password += ' '
            else:
                password += '#'
        answer.append(password)
    return answer