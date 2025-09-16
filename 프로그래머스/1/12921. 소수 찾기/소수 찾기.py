def solution(n):
    answer = 0
    primes = [1] * (n + 1)
    primes[0] = primes[1] = 0
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] == 1:  
            for j in range(i * i, n + 1, i):
                primes[j] = 0
    
    answer = sum(primes)
    return answer