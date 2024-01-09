def solution(s):
    s=s.split(" ")
    answer = 0
    for i in range(len(s)) :
        if s[i] == 'Z' :
            answer-= int(s[i-1])
            continue
        answer += int(s[i])
    return answer