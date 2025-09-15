def solution(n, m, section):
    answer = 0
    end = 0  # 현재 롤러로 덮을 수 있는 끝 위치
    
    for s in section:
        if s > end:  # 아직 덮이지 않은 시작점 발견
            answer += 1
            end = s + m - 1  # 새로운 롤러 칠하기
    return answer
