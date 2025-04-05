import sys

input = sys.stdin.readline

n = input().split(sep="-")

total = sum(map(int,n[0].split(sep = "+")))

for x in n[1:]:
    total -= sum(map(int,x.split(sep = "+")))

print(total)