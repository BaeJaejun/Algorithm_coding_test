import sys

input = sys.stdin.readline

x,y,w,h = map(int,input().split())

print(min(min(w - x, x), min(h - y,y)))