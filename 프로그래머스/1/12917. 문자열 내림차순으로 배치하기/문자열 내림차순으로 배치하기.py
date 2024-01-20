def solution(s):

#   'A' = 65
#   'a' = 97
    
    s = list(s)
    answer = sorted(s,key=lambda x:ord(x), reverse=True)
    answer = ''.join(answer)
    return answer