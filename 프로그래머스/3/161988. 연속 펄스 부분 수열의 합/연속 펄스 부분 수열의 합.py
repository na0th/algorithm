def solution(sequence):
    '''
    연속 부분 수열의 합?
    펄스 부분 수열이 아니면 원래는 어떻게 최대 부분 수열 합을 구하지..
    카데인?
    
    current_sum = max(max(cureent까지 펄스수열 최대에 +나 -나), max(+나 -나))
    
    이전 펄스수열 최대에서 
    
    max_value(역대 최대) = max(max_value,current_sum)

    
    문제 : 근데 계속 기억해야 할 것 같은데 
    
    def 퐁당퐁당 ():
        // +1부터 시작
        
        // -1부터 시작
        return sum1,sum2
    '''
    
    pulse1 = [(num if i % 2 == 0 else -num) for i, num in enumerate(sequence)]
    pulse2 = [(-num if i % 2 == 0 else num) for i, num in enumerate(sequence)]
    
    # print(pulse1)
    # print(pulse2)
    
    def kadane(arr):
        current_sum = arr[0]
        max_sum = arr[0]
        
        for num in arr[1:] :
            current_sum = max(num,current_sum+num)
            max_sum = max(max_sum,current_sum)
            
        return max_sum
    
    max_sum1 = kadane(pulse1)
    max_sum2 = kadane(pulse2)
    
    return max(max_sum1,max_sum2)
    