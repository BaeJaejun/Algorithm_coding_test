import sys
from collections import defaultdict
input = sys.stdin.readline

while (True):   
    m = int(input().strip())
    if m == 0:
        break
    sen = input().strip()
    
    max_len = 0
    length =len(sen)
    
    # O(N^2) or set(list) n 시간이라 O(N^3) 일수도? 시간초과
    # for i in range(length-m+1):
    #     for j in range(m,length):
    #         if len(set(sen[i:j])) <= m:
    #             max_len = max(max_len,j-i-1)
    #         else:
    #             break
    
    freq = defaultdict(int)
    unique = 0
    end = 0
    start = 0
    
    for end in range(length):
        if freq[sen[end]] == 0:
            unique += 1
        freq[sen[end]] += 1

        while unique > m:
            freq[sen[start]] -= 1
            if freq[sen[start]] == 0:
                unique -= 1
            start += 1 

        cur_len = end - start + 1
        max_len = max(max_len,cur_len)
    
    print(max_len)    