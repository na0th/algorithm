def solution(s):
    capital=[]
#   'A' = 65
#   'a' = 97
    
    print(ord('a'))
    
    s = list(s)
    print(s)
    answer = sorted(s,key=lambda x:ord(x), reverse=True)
    print(answer)
    answer = ''.join(answer)
    return answer