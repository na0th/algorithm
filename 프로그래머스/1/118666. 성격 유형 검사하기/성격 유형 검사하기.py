def solution(survey, choices):
#   같을 때는 사전순이다..
#   AN인데 5면 ?   N에 1점
#   CF인데 3이면?  C에 1점
    
    #       딕셔너리에 추가하기 모든 값을 0
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
   
    for idx,item in enumerate(survey) :
        print(idx,item)
        each_survey = list(item)
#       ['A','N'] 꼴

#       1,2,3이면 앞에 거에 choice를 더한다.
        if choices[idx] in [1,2,3] :
            dic[each_survey[0]]+=4-choices[idx]
#       5,6,7이면 뒤에 거에 choice%4를 더한다. ex) 5 -> 1 , 6 -> 2 , 7 -> 3
        if choices[idx] in [5,6,7] :
            dic[each_survey[1]]+=(choices[idx]-4)
    

    print(dic)
    
    answer = ''
    
  # 맨처음 문항부터 조합하기.
    if dic['R'] >= dic['T'] :
        answer+='R'
    else :
        answer+='T'
    
    if dic['C'] >= dic['F'] :
        answer+='C'
    else :
        answer+='F'
    
    if dic['J'] >= dic['M'] :
        answer+='J'
    else :
        answer+='M'
        
    if dic['A'] >= dic['N'] :
        answer+='A'
    else : 
        answer+='N'
        
        
    
    return answer