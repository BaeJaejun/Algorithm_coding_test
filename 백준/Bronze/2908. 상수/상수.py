import sys

input = sys.stdin.readline

a,b = map(str,input().split())

A = a[::-1]
B = ''.join(reversed(b))

print(max(int(A),int(B)))