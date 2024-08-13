def solution(gems):
    from collections import Counter
    from collections import defaultdict
    '''
    진열된 모든 종류의 보석을 적어도 1개이상 포함하는 가장 짧은 구간
    
    투포인터로 푼다면?
    if 종류수가 적어 right +1
    if 종류수랑 같은데? 그럼 왼쪽 +1 해봐 그러다 종류수가 적어진다면? 추가 그떄의 left,right 인덱스 append
    
    
    '''


    n = len(set(gems))  
    if n == 1:
        return [1, 1]
    
    counter = Counter()
    left, right = 0, 0
    found, idx_list = 0, [] 

    while right < len(gems):
        if counter[gems[right]] == 0:
            found += 1
        counter[gems[right]] += 1
        right += 1
        
#       일단은 모든 종류를 포함하는데 여기서 n을 만족시키는 동안까지 left를 당긴다
        while found == n:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                found -= 1
            left += 1
            idx_list.append([left,right])

    idx_list.sort(key=lambda x:(x[1]-x[0],x[0]))
    return idx_list[0]
