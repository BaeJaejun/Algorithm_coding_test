import sys

input = sys.stdin.readline

           # 0 1 2 3 4 5 6 7 8 9
torch_cnt = [6,2,5,5,4,5,6,3,7,6]  # 2 3 4 5 6 7  사용

n = int(input().strip())

n = n - 4 # += 개수 빼주기

def cnt_t(x):
    cnt_x = 0
    if x < 10:
        cnt_x = 6 + torch_cnt[x]  
    else:
        cnt_x = torch_cnt[int(str(x)[0])]+ torch_cnt[int(str(x)[1])]
    return cnt_x


def sol():
    if n <= 0:
        return False

    for i in range(100):
        for j in range(100):
            a = i 
            b = j
            c = a + b
            if c > 99:
                continue
            result = cnt_t(a) + cnt_t(b) + cnt_t(c)
            
            if result == n: 
                print(f"{a:02d}+{b:02d}={c:02d}")
                return True
            
if not sol():
    print("impossible")
    