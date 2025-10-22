from collections import defaultdict
def solution(X, Y):
    answer = ''
    dictX = defaultdict(int)
    dictY = defaultdict(int)
    
    result = []
    for i in X:
        dictX[i] += 1
    
    for i in Y:
        dictY[i] += 1
        
    for i in range(10):
        count = min(dictX[str(i)], dictY[str(i)])
        result.extend([str(i)] * count)
        
    
    result.sort(reverse = True)
    answer = ''.join(result)

    if not result:
        return "-1"
    if result[0] == '0':
        return '0'

    
    return answer