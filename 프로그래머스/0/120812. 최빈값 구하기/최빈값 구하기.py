def solution(array):
    from collections import Counter
    cnt = Counter(array)
    
    # cnt = sort(cnt.items(),key=lambda x:x[0],reverse=True)
    
    print(cnt)
    
    if len(cnt) >= 2 :
        print(cnt.most_common(),'!')
        if cnt.most_common()[0][1] == cnt.most_common()[1][1] :
            return -1
        else :
            return cnt.most_common()[0][0]
    else :
        return cnt.most_common()[0][0]
    