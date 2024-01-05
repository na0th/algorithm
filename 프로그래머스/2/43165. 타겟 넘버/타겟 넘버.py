def solution(numbers, target):
    from itertools import combinations, permutations

    # nums = [1,2,3,4]
    # combi = list(combinations(nums, 2))
    
#   숫자 개수가 20까지면 2^20개 = 1000 * 1000 = 10^6이면 완전탐색 가능?
#   조합을 이용해야 한다..
    cnt = 0
    for i in range(len(numbers)):
        combi = list(combinations(numbers,i+1))
        for combo in combi :
            if -2 * sum(combo) + sum(numbers) == target :
                cnt+=1
    print(cnt)            
        
    
    return cnt