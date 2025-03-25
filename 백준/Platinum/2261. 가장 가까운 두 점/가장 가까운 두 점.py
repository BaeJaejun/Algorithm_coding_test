import sys
import math
input = sys.stdin.readline

N = int(input().strip())

matrix = []
for _ in range(N):
    x,y = map(int,input().split())
    matrix.append((x,y))
    
matrix.sort()

left = 0
right = N-1

def merge(left,right,l_dis,r_dis):
    #합쳤을때의 최소 거리   
    d = math.sqrt(min(l_dis,r_dis))
    arr = left + right
    midx = arr[len(arr)//2][0] # 중간 x값
    
    re =[]
    m_dis = float('inf')

    for i in range(len(arr)):
        if midx-d <= arr[i][0] <= midx+d:
          re.append(arr[i])
          
    arry = sorted(re,key= lambda x: x[1]) # y기준 정렬
    
    for i in range(len(arry)):
        for j in range(i+1,len(arry)):
            if (arry[i][1]-arry[j][1])**2 >= d**2:
                break
            m_dis = min(m_dis,(arry[i][0]-arry[j][0])**2 + (arry[i][1]-arry[j][1])**2)
      
    return arr , min(l_dis,r_dis,m_dis)

    
def divide(matrix):
    if len(matrix) <= 3:
        mini = float('inf')
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                mini = min(mini, (matrix[i][0]-matrix[j][0])**2 + (matrix[i][1]-matrix[j][1])**2)
                 
        return matrix, mini
    
    mid = len(matrix) // 2
    left = matrix[:mid]
    right = matrix[mid:]
    
    left_,l_dis = divide(left)
    right_,r_dis = divide(right)
    return merge(left_,right_,l_dis,r_dis)

print(divide(matrix)[1])