import sys

input = sys.stdin.readline

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

for _ in range(int(input().strip())):
    num = int(input().strip())
    
    if is_prime(num//2):
        print(f'{num//2} {num//2}')
    else:
        a = num//2
        b = num//2
        while True:
            a = a + 1
            b = b - 1
            if is_prime(a) and is_prime(b):
                print(f'{b} {a}')
                break

    