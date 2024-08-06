def solution(n):
    '''
    나누어 떨어지면 몫으로 보내야 하는데
    ex 12면
    n 12를 3으로 나누면 q는 원래는 4지만 3..3으로 표현
    그 q가 다시 n이되고 3으로 나누어 떨어지니까 0..3 으로 표현해서 033인데 0빼
    
    
    '''
    from collections import deque
    
    answer = deque()
    while(n > 0) :
        if (n%3) == 0 :
            q = (n // 3) -1
            m = 3
            n = q
        else :
            q = n // 3 
            m = n % 3
            n = q
        answer.appendleft(m)
    
    for i,item in enumerate(answer) :
        if item ==  3 :
            answer[i] = 4
            
    answer = map(str, answer)
    
    return ''.join(answer)