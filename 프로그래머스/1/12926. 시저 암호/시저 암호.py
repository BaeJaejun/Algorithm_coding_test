def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            base = ord('A') if i.isupper() else ord('a')
            answer += chr((ord(i) - base + n) % 26 + base)
        else:
            answer += ' '
    return answer