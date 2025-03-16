import sys

input = sys.stdin.readline

def sol():
    for i in range(9):
        for j in range(i+1, 9):
            if sumh - h[i] - h[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(h[k])
                return     
            
h = []
for _ in range(9):
    h.append(int(input()))


h.sort()
sumh = sum(h)

      
sol()