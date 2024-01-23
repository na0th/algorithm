def solution(s):
    split = s.split(" ")
    split = list(map(int,split))
    answer = ''
    answer=str(min(split))+' '+str(max(split))
    return answer