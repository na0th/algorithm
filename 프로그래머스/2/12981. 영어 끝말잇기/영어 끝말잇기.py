def solution(n, words):

    dict = {}
    recent_last_words = ''
    for idx,word in enumerate(words) :
        #       마지막 철자와 다른 알파벳으로 시작한 경우 break
        if recent_last_words != '':
            if recent_last_words != word[0]:
                return [(idx)%n+1,((idx)//n)+1]
            recent_last_words = word[-1]
        if recent_last_words == '' :
            recent_last_words= word[-1]
            
#       딕셔너리에 word 등록    
        if word not in dict :
            dict[word] = 1
            continue
#       딕셔너리에 word가 있는 경우(중복 선언) break
        if word in dict :
            return [(idx)%n+1,((idx)//n)+1]
            
    return [0,0]
            
#  중복 제거를 위한 딕셔너리 
#   return은 words개수와 n을 나머지 몫을 통해서 리턴하면 될 것 같다.
