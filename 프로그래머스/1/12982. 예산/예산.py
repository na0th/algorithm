def solution(d, budget):
    d.sort()
    print(d)
    answer = 0
    for item in d :
        if budget-item >= 0 :
            budget-=item
            answer+=1
    
    return answer