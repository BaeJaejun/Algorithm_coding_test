import sys

sys.stdin.readline

poly = input().strip()

# -6+6x
for i,k in enumerate(poly):
    if k == 'x':
        if i == 0:
            print(1)
            break
        elif i == 1 and poly[0] == '-':
            print(-1)
            break
        else:
            print(poly[:i])
            break

if 'x' not in poly:
    print(0)
