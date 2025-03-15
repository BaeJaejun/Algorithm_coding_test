import sys

input = sys.stdin.readline

n = int(input().strip())
words = set()
s_words = []
longest = 0
for _ in range(n):
    word = input().strip()
    if longest < len(word):
        longest = len(word)
    words.add(word)

list(words)
   
for i in range(1,longest + 1):
    a = []
    for k in words:
        if i == len(k):
            a.append(k)
    for k in sorted(a):
        print(k)
        
    
