def solution(s):
    answer = ''
    dict = {'zero': 0 , 'one' : 1, 'two': 2, 'three' : 3, 'four': 4,
            'five' : 5, 'six' : 6, 'seven' : 7, 'eight': 8, 'nine': 9}
    
    x = ''
    for a in s:
        if a.isdigit():
            answer += a
        else:
            x += a
            
        if x in dict:
            answer += str(dict[x])
            x = ''
    
    return int(answer)