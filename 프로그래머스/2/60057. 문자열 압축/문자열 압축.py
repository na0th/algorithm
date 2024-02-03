def solution(s):
#   완전탐색으로 처음부터 전부 뒤져서 min 값 리턴하기
#    1개로 자르기, 2개로 자르기.... n개로 자르기

#   [ [1,'abc'],[2,'bbb'] ]  이런 형태로 추가하기
#    [-1][1]이 있는지 체크해서 있으면 [-1][0]에 +1
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
#       카운팅 숫자가 2일 때는 1개 자리수 차지, 20일때는 2개 자리수 차지..
            if cnt_list[q][0] != 1 :
                cnt += len(str(cnt_list[q][0]))
            cnt += len(cnt_list[q][1])
                
        answer.append(cnt)
        
    # print(min(answer))
    return min(answer)