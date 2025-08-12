def solution(x, n):
    answer = []
    plus = x
    for _ in range(n):
        answer.append(int(x))
        x = x + plus
    return answer