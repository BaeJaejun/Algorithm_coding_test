import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

N = int(input().strip())

cards = []

for _ in range(N):
    heappush(cards,int(input().strip()))
    
sumC = 0

while len(cards) > 1:
    hap = heappop(cards) + heappop(cards)
    sumC += hap
    heappush(cards,hap)

print(sumC)