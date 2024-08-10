def solution(triangle):
    '''
    IF 그 줄에서 첫 번째 OR 마지막이 아니면
    그 윗줄의 0~1번중  MAX가 다음줄의 1번을 결정, 윗줄의 1~2번중 MAX가 다음 줄의 2번 결정
    .... 그렇게 쭉..
    
    
    
    '''
    for k,item in enumerate(triangle) :
        # print(item)
        for i in range(len(item)) :
            if k > 0 :
                if i == 0 :
                    # print("k=",k,"triangle",triangle[k-1][0])
                    item[i] = triangle[k-1][0] + item[i]
                    # print(item[i],end=' ')
                elif i == len(item)-1 :
                    item[i] = triangle[k-1][i-1] + item[i]
                    # print(item[i],end=' ')
                else : 
                    item[i] = max(triangle[k-1][i-1],triangle[k-1][i]) +item[i]
                    # print(item[i],end=' ')
    
                
        # print()
    # print(triangle)
    return max(triangle[-1])