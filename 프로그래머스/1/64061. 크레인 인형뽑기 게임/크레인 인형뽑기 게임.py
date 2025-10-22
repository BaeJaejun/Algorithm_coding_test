def minus(x):
    return x-1

def solution(board, moves):
    answer = 0
    result = [-1]
    
    move = list(map(minus,moves))
    
    for m in move:
        for i in board:
            if i[m] != 0:
                if result[-1] == i[m]:
                    result.pop()
                    answer += 2
                else:
                    result.append(i[m])
                i[m] = 0
                break
                
    return answer