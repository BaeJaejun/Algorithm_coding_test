def solution(numbers, hand):
    answer = ''
    position = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    lh = position['*']
    rh = position['#']
    
    left = [1,4,7]
    right = [3,6,9]
    
    for i in numbers:
        if i in left:
            lh = position[i]
            answer += 'L'
        elif i in right:
            rh = position[i]
            answer += 'R'
        else:
            target = position[i]
            l_dist = abs(lh[0] - target[0]) + abs(lh[1] - target[1])
            r_dist = abs(rh[0] - target[0]) + abs(rh[1] - target[1])
            
            if l_dist < r_dist:
                answer += 'L'
                lh = target
            elif r_dist < l_dist:
                answer += 'R'
                rh = target
            else:
                if hand == 'right':
                    answer += 'R'
                    rh = target
                else:
                    answer += 'L'
                    lh = target
                    
    return answer