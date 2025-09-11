from heapq import heapify,heappush, heappop

def solution(k, score):
    answer = []
    kkk = []
    heapify(kkk)
    
    for i in score:
        if len(kkk) < k:
            heappush(kkk,i)
        else:
            if kkk[0] < i:
                heappop(kkk)
                heappush(kkk,i)
        
        answer.append(kkk[0])
        
    return answer