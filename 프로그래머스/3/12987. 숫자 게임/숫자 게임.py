def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    # print(A)
    # print(B)
    count = 0
    
    k = 0
    i = 0
    while(True):
        
        if k == len(A)-1 :
            if B[i] > A[k] :
                count+=1
            break   
            
        if B[i] > A[k] :
            count+=1 
            k = k+1
            i += 1
            continue
        

#       k는 계속 변화    
        k += 1 
#       종료조건 

    
    answer = count
    return count