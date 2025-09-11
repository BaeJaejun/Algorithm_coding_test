def solution(a, b):
    answer = ''
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = day[(sum(month[:a]) + b) % 7 - 1]
    return answer