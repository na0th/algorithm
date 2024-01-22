def solution(id_list, report, k):
#   1번에 1명 신고, 여러번 신고 가능, but 동일 유저면 신고 1회처리
#   k번이상 신고시 게시판 정지 후 유저를 신고한 모든 유저에게 정지 사실 발송

#   report 1개를 읽어서 split으로 공백 기준으로 2개 나눈 후에
#   dic1에 report(split)[0] = report(split)[1]으로 등록하고
#   ex) muzi: [frodo,apeach,neo]
#   dic2에 report(split[1]) +=1 한다 ..
#   다 한다음 다시 dic2를 for문 순회하면서 k 넘는 것 있으면 list에 key를 담아..
#   ex) frodo : 3 , apeach : 4 ..  => [frodo,apeach]
#   다시 돌면서 딕셔너리의  muzi: [frodo,apeach,neo]에서 value 리스트를 for문으로 돌면서 in key_list 면 +=1 해서 answer.append 후 리턴..
    dic1 = dict()
    dic2 = dict()
    
    for id_ in id_list :
        dic1[id_] = []
        dic2[id_] = 0
    
    
    for item in report :
        split = item.split(" ")
        # if split[0] not in dic1 :
        if split[1] in dic1[split[0]]:
            continue
        dic1[split[0]].append(split[1])
        
        if split[1] not in dic1[split[0]] :
            dic1[split[0]].append(split[1])
            
        # if split[1] not in dic2 :
        #     dic2[split[1]] = 1
        # else :
        # if split[1] in dic1[split[0]] :
        #     dic2[split[1]] -=1
        dic2[split[1]] +=1

        # elif split[1] not in dic1[split[0]]:
        #     dic2[split[1]] += 1
            
    # print(dic1)
    # print(dic2)
    
    
    report_list=[]
    for key,value in dic2.items() :
        if value >= k :
            report_list.append(key)
            
            
    # print(report_list,"report_list")
    
    answer = []
    
    
        
    # print(dic1,5)
    for key,value in dic1.items():
        cnt = 0
        for item in value :
            if item in report_list :
                cnt+=1
        answer.append(cnt)
        # print(answer)
        
    
    return answer