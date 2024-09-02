def solution(k, m, score):
    '''
    사과 한 상자 가격은 p*m
    
    k= 3, m= 4 라면
    3~k~9 , 3~m~10
    '''
    score.sort(reverse=True)
    # print(score)
    result = []

    total = 0
    for j in range(0,len(score),m):
        temp = score[j:j+m]
        if len(temp)< m :
            continue
        total += min(temp)*len(temp)
        # print(score[j:j+m])
        # print()
    result.append(total)
    # print(result)
    return max(result)