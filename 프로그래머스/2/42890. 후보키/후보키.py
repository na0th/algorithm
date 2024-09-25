def solution(relation):
    from itertools import combinations
    from collections import Counter
    '''
    유일성과 최소성을 만족시키는 것이 후보키 =  and 조건
    컬럼의 길이가 8이하다.. 이정도면 조합 만들어서 유일하게 식별되는지 체크해도 되지않나..
    
    1개짜리 2개짜리 3개짜리 ... 최대 8개짜리 조합을 만들어서
    유일성 : counter해서 모두 1인지 확인
    
    최소성 : 2개조합부터는 자신-1개짜리 통과한 조합을 다 뒤져서,
    자신이랑 교집합 개수가 자신-1개인 조합이 있다 
    -> 통과한 조합 중 추가돼서 만들어진 집합이니 최소성 X
    
    
    '''
    

    
    row = len(relation)
    col = len(relation[0])
    
    nums = [i for i in range(col)]
    unique = set()
    for i in range(col):
        #1개짜리 조합, ~~ n개짜리 조합 다 나옴
        comb = combinations(nums, i+1)
        result = [list(c) for c in comb]
        for item in result :
            temp = []
            for r in range(row) :
                selected_values = tuple(relation[r][col_idx] for col_idx in item)
                temp.append(selected_values)
            
            temp = Counter(temp)
            
    
            # 유일성
            if len(temp) == row :
                # 최소성 
                if not any(set(existing).issubset(item) for existing in unique):
                    unique.add(tuple(item))


    return len(unique)



    
    