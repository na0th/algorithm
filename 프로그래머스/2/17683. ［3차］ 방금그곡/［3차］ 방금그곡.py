def solution(m, musicinfos):
    """
    음악 제목, 시작과 끝 시각, 악보
    음은 1분에 1개씩 
    음악은 처음부터 재생되고, 재생 시간이 길면 다시 처음부터 반복
    음악은 최대 1439개의 악보 
    리턴 : 조건 일치 음악이 여러개면 제일 긴 음악제목 리턴 
    AND
    재생 시간이 같으면 먼저 입력된 음악 제목 리턴
    조건 일치 음악이 없으면 NONE 반환
    
    음을 일단 music infor에 대해 queue만들어서 m번만큼 확인 넣어서 뒤로..
    
    
    
    """
    
    
#   치환..
    dic = {'C':'C','C#':'c','D':'D','D#':'d',
          'E':'E','F':'F','F#':'f','G':'G','G#':'g','A':'A','A#':'a','B':'B'
          }
    
    def trans(word):
        trans_word = ''
        for i in range(len(word)-1):
            wd = ''
            if word[i] != '#' and word[i+1] == '#' :
                wd += (word[i]+word[i+1])          
            elif word[i] != '#' and word[i+1] != '#' :
                wd += word[i]
            if wd in dic :
                trans_word += dic[wd]
        if word[-1] != '#' :
            trans_word+=dic[word[-1]]
            
        return trans_word
    
    # print("trans",trans(m))

    answer = []
    for item in musicinfos : 
        element_list = item.split(",")
        
        time_start_list = element_list[0].split(":")
        time_start = int(time_start_list[0])*60 + int(time_start_list[1])   

        time_end_list = element_list[1].split(":")
        time_end = int(time_end_list[0])*60+ int(time_end_list[1])

        time_diff = time_end - time_start

        # print("세기",cnt_pitch)
        trans_word = trans(m)
        trans_music = trans(element_list[3])
        
        len_m = len(trans_word)
        len_music = len(trans_music)
        # print("len_m,len_music",len_m,len_music)
        
        
        val = ''
        q = time_diff // len_music
        mod = time_diff % len_music
        # print("q,mod",q,mod)
        
        if  q >= 1 :
            val = trans_music  * q + str(trans_music[:mod])
        else :
            val = str(trans_music [:mod])
        # print("val=",val)
        
        
        if trans_word in val :
            # print("포함")
            answer.append([element_list[2],time_diff,time_start])
        # print(answer)
        answer.sort(key=lambda x: (-x[1],x[2]))
        
    if not answer :
        return "(None)"

    return answer[0][0]
        
   
