def solution(sequence, k):
    '''
    비내림차순 = 같을 때를 포함하는 오름차순
    리턴 : 합이 k인 부분수열중 가장 길이가 짧은 수열
    and 길이도 같다면 인덱스가 작은 수열을 리턴
    
    sequence 길이가 10^6
    result= [] 선언 
    start = 0 , end = 0 시작하고 sum[start,end]가 k보다 작으면 end +=1
    크면 start -1 이렇게 가보자
    
    '''
    result = [] 
    start, end = 0, 0
    cur_sum = sequence[0]
    min_len  = 10000001
    
    while end < len(sequence) : 
        
        if cur_sum == k :
            if end-start < min_len :
                min_len = end-start
                result = [start, end]
            cur_sum -= sequence[start]
            start+=1
            
        elif cur_sum > k :
            cur_sum -= sequence[start]
            start+=1
        elif cur_sum < k :
            end+=1
            if end < len(sequence) :
                cur_sum += sequence[end]
            
            
    
    return result