def solution(data, ext, val_ext, sort_by):
    answer = []
    base = ['code','date', 'maximum', 'remain']
    
    for x in data:
        if x[base.index(ext)] < val_ext:
            answer.append(x)
            
    answer.sort(key = lambda x :(x[base.index(sort_by)]))
    return answer