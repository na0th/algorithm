def solution(s):
    from collections import deque
#   데크 
    deq = deque()
    for i in range(len(s)):
#       홀수면 보지도 않고 틀렸다.
        if len(s) % 2 == 1 :
            return False
#       스택으로 "(" 나오면 push
        if s[i] == "(" :
            deq.append("(")
#       스택으로 ")" 나오면 스택에서 제거 (없으면 안하도록 예외처리)
        elif "(" in deq and s[i] == ")":
            deq.remove("(")
        
#   그래서 쌍이 잘 맞아서 전부 지워졌으면 True 아니면 False 리턴
    if not deq :
        return True
    if deq :
        return False
    