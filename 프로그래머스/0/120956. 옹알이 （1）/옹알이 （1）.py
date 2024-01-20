
#   순열로 4p1 =4, 4p2 = 12, 4p3 = 24, 4p4  = 24
#   딕셔너리에 넣고 카운팅
import itertools
def solution(babbling):
    
    dic = dict()
    
    can_say =["aya","ye","woo","ma"] 
    all_babbling = []
    
    for i in range(1,5):
        npr = itertools.permutations(can_say,i)
        
        for item in npr :
            temp = "".join(item)
            dic[temp]=1
    
    cnt = 0
    
    for item in babbling :
        if item in dic :
            cnt+=1

    
    return cnt