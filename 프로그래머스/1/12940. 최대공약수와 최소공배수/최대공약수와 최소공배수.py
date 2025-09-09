def solution(n, m):
    answer = []
    minx = min(n,m)
    gcd = 0
    lcm = 0
    for i in range(1,minx+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    
    for i in range(1, n*m+1):
        if i  * gcd % n == 0 and i * gcd % m == 0:
            lcm = i* gcd
            break
    answer.append(gcd)
    answer.append(lcm)
    return answer