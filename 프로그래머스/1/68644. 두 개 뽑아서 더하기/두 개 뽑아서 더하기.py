def solution(numbers):
    answer = set()
    
    for i,k in enumerate(numbers[:-1]):
        for j in range(i+1,len(numbers)):
            answer.add(k+numbers[j])
            
    
    return sorted(list(answer))