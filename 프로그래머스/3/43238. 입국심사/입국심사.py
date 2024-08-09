def solution(n, times):
    import sys
    
    left = 0 
    right = 100000000000000000000000
    
    while True :
        mid = (left+right) // 2
        sum_add_q = sum(mid // time for time in times)
        if sum_add_q >= n  :
            right = mid -1
            q_add_front = sum((mid-1)//time for time in times)
            if q_add_front < n :
                return mid
        else :
            left = mid + 1
        
#         else : 
#             q_add_front = sum((mid-1)//time for time in times)
#             q_add_back = sum((mid+1)//time for time in times)
            
#             if q_add_front < n :
#                 return mid
#                 break
#             if q_add_back == n :
#                 right = mid -1
            
            