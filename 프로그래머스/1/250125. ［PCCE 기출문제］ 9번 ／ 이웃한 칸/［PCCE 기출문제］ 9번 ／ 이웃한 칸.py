def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [1,-1,0,0]
    dw = [0,0,1,-1]
    
    for i in range(4):
        nh = dh[i] + h
        nw = dw[i] + w
        
        if 0 <= nh < n and 0 <= nw < n and board[h][w] == board[nh][nw]:
            answer += 1
            
    return answer