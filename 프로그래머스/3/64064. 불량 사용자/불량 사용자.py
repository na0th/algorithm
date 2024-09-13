def solution(user_id, banned_id):
    from collections import defaultdict
    '''
    불량사용자를 당첨 처리에서 제외해야 함
    사용자 아이디를 '*' 문자로 가렸음 1글자당 1개로

    백트래킹인가?
    
    
    '''
    
    def match(a,b):
        if len(a) == len(b) :
            for i in range(len(b)) :
                if b[i] == '*' :
                    a = list(a)
                    a[i]='*'
                    a=''.join(a)
            if a == b :
                return True
        return False
    # print(match("frodo","fr*d*"))
    
    dic = defaultdict(set)
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if match(user_id[i],banned_id[j]) == True :
                dic[banned_id[j]].add(user_id[i])
    print(dic)
    def backtrack(banned_id, idx, current_set, result):
        # 종료 조건
        if idx == len(banned_id):
            result.add(tuple(sorted(current_set)))
            return

        for user in dic[banned_id[idx]]:
            if user not in current_set:
                 # 백트래킹 (넣은 다음 돌려보고 다시 빼기)
                current_set.add(user)
                backtrack(banned_id, idx + 1, current_set, result)
                current_set.remove(user) 
        
    result = set()
    backtrack(banned_id, 0, set(), result)
    return len(result)
