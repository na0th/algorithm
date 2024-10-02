def solution(scores):
    from collections import defaultdict
    from collections import Counter
    '''
    각 사원마다 근무 태도 점수, 동료 평가 점수가 기록
    어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면
    -> 인센티브 X
    
    그렇지 않은 사원들은 두 점수의 합으로 석차에 따라 차등 지급
    동석차는 건너뛴다. 11 다음은 3등 
    
    첫 번째가 완호의 점수인데, 완호의 석차를 return
    인센티브를 받지 못하는 경우 -1을 리턴
    
    a,b의 합이 c,d의 합보다 크다면
    
    (a,c) (b,d) 중 하나는 왼쪽이 크다는 뜻, 둘 다 오른쪽보다는 작을 수 없다..
    
    즉, 나보다 [근무태도점수,동료평가점수]의 합이 존재한다면 나는 인센티브를 받을 수 있다는 뜻
    근데 그 안에서 나보다 작은 친구가 없을 때 인센티브를 받을 수 있는지?
    아니면 같다면?

    
    1. 일단 scores를 돌면서 점수의 합을 계산해놓는다.
    2. 낮은 순으로 정렬하고, 완호의 점수 합이 min 값이랑 같으면 -1리턴 ?? 
    3. 아니면 석차를 계산해야 하는데.. Counter를 써서 합이 큰 순으로 석차(value)를 더한다
        그러다 완호의 합이 나오면 석차를 리턴한다.
        
    
    정렬을 해서 
        
    
    '''
    wanho_left = scores[0][0]
    wanho_right = scores[0][1]
    
    wanho = scores[0][0]+scores[0][1]
    i_min, j_min = scores[0][0],scores[0][1]
    
    scores.sort(key=lambda x:(-x[0],x[1]))
    # print(scores)
    
    max_b = -1
    filter_list = []
    for i, (a,b) in enumerate(scores):
        if b >= max_b :
            filter_list.append((a,b))
            max_b = b
    # print("filter",filter_list)
    if (wanho_left,wanho_right) not in filter_list :
        return -1
    sum_score_list = [a + b for a, b in filter_list]
    # print(sum_score_list)
    sum_score_list.sort(reverse=True)
    # print(sum_score_list)   
    
    rank = 1 
    for score in sum_score_list :
        if score == wanho :
            return rank
        rank += 1
    
    return rank
    

            

