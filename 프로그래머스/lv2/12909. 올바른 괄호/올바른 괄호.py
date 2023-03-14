def solution(s):
    from collections import deque
    
    answer = False
    
    deq = deque()
    for i in range(len(s)):
        if len(s) % 2 == 1 :
            return False
        if s[i] == "(" :
            deq.append("(")
        elif "(" in deq and s[i] == ")":
            deq.remove("(")
        
    
    if not deq :
        return True
    if deq :
        return False
    