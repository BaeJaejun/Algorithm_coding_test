def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if cards1 and i == cards1[0]:
            cards1.remove(i)
        elif cards2 and i == cards2[0]:
            cards2 = cards2[1:]
        else:
            answer = 'No'
            break
    return answer