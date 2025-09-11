def solution(nums):
    answer = 0
    x = len(nums)//2
    
    if x <  len(set(nums)):
        answer = x
    else: 
        answer = len(set(nums))
    
    return answer