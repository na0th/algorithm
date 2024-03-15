def solution(scoville, K):
    import heapq
    
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >=1 :
#       다 합쳐도 작은 경우 (끝내기)
        if len(scoville)==1 and scoville[0] < K :
            return -1
#       다 큰 경우 (끝내기)
        if  scoville[0] >= K :
            return cnt
        else :
            num1 = heapq.heappop(scoville)
            num2 = heapq.heappop(scoville) * 2
            
            new_num = num1+num2 
            heapq.heappush(scoville,new_num)
            
            cnt+=1
        

