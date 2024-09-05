def solution(n, stations, w):
    import math 


    '''
    전체 배열 만들고
    stations 원소들 w에 맞게 0으로 만들어버리기
    
    
    그다음 for문으로 배열 순회하면서 1 만나면? 앞에서부터 0 만들기(그리디하게)
    끝나는 건 len(array)-1에 닿으면 끝
    '''

    result = []
    if not stations :
        result.append(n)
        return math.ceil(result[-1]/(1+2*w))
    result.append(stations[0]-1-w)
    for i in range(len(stations)-1) :
        result.append(stations[i+1]-stations[i]-(2*w+1))
    result.append(n-stations[-1]-w)
    # print(result)
    for i in range(len(result)) :
        # print(result[i])
        result[i] = math.ceil(result[i]/(1+2*w))
    
    # print(result)
    return sum(result)
        
       
        
    
    
    