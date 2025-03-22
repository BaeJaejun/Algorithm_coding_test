import sys

input = sys.stdin.readline

while True:
    #입력 받기
    h = list(map(int,input().split()))
    n, H = h[0] , h[1:] # 리스트 길이, 높이 리스트
    if n == 0:
        break
    
    # 문제 해결
    # 완전 탐색 (시간 초과)
    # max_extent = 0
    # for h in range(1,max(H)+1):
    #     cnt = 0
    #     for j in H:
    #         if j >= h:
    #             cnt += 1
    #         else:
    #             extent = cnt * h
    #             cnt = 0
    #             max_extent = max(max_extent,extent)
        
    #     if cnt > 0:
    #         extent = cnt * h
    #         max_extent = max(max_extent,extent)
   
    
    # print(max_extent)
    
    
    # 분할정복
    def merge(l,r,l_extent,r_extent):
        global max_extent       
        # 합쳤을 때 넓이 =
        #l의 가장 우측 인덱스부터 + r의 가장 좌측 인덱스부터
        #합쳐서 넓이 구하기
        
        m_extent = 0
        h = min(l[len(l)-1],r[0]) # 가운데 초기 높이
        m_extent = h*2
        pl = len(l)-1
        pr = 0
        while pl > 0 or pr < len(r) -1 :
            if pr < len(r)-1 and (pl == 0 or r[pr + 1] >= l[pl - 1]):
                pr += 1
                h = min(h,r[pr])
            elif pl > 0:
                pl -= 1
                h  = min(h,l[pl])
            else:
                break
            width = (len(l) - pl) + pr + 1
            area = h * width
            
            m_extent = max(area, m_extent) 
        
        #리스트 합쳐서 반환
        merge_list = l + r
               
        # 좌,우,합침 리스트 중 가장 큰 넓이 반환
        merge_extent = max(l_extent,r_extent,m_extent)
        return merge_list, merge_extent
        
        
    def sol(u_list):
        if len(u_list) <= 1:
            extent = u_list[0] * 1
            return u_list, extent
        
        mid = len(u_list) // 2
        left = u_list[:mid]
        right = u_list[mid:]
        
        left_li, left_extent = sol(left)
        right_li, right_extent = sol(right)
        return merge(left_li,right_li, left_extent, right_extent)
            
    x,y = sol(H)
    print(y)