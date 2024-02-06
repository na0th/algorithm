def solution(nums):
    answer = -1

    def is_prime(num):
        for i in range(2,num) :
            if num % i == 0 :
                return False
        return True
    
    from itertools import combinations
    
    cnt = 0 
    combo = list(combinations(nums,3))
    for combi in combo :
        if is_prime(sum(combi)) == True :
            cnt+=1
        # print(sum(combi))

    
    return cnt