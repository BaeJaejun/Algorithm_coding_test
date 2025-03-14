import sys

input = sys.stdin.readline

A,B,V = map(int,input().split())

v = V - A
up = A-B

print(v // up + (1 if v % up > 0 else 0) + 1)