def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        x = []
        for c,d in zip(a,b):
            x.append(c+d)
        answer.append(x)
    return answer