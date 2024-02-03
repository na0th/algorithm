def solution(s):
    answer = []
    for k in range(1,len(s)+1):
        cnt_list = []
        cnt = 0
        for i in range(0,len(s)+1,k):
            # print(s[i:i+k])
            if not s[i:i+k] :
                continue
            
            if not cnt_list :
                cnt_list.append([1,s[i:i+k]])
                continue
            
            if cnt_list[-1][1] == s[i:i+k] :
                cnt_list[-1][0] += 1
            else :
                cnt_list.append([1,s[i:i+k]])
                
        # print(cnt_list)
        # print()
        
        for q in range(len(cnt_list)):
            if cnt_list[q][0] != 1 :
                cnt += len(str(cnt_list[q][0]))
            cnt += len(cnt_list[q][1])
                
        answer.append(cnt)
        
    # print(min(answer))
    return min(answer)