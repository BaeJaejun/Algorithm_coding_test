def solution(nums):
    answer = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                x = nums[i] + nums[j] + nums[k]
                if x % 2 == 0:
                    continue
                    
                z = 0
                
                for y in range(2, x):
                    if x % y == 0:
                        break
                    z = y   
                    
                if z == x-1:
                    answer += 1
    return answer