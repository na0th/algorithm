def solution(fees, records):
#   기본 시간, 기본 요금, 단위 시간, 단위 요금
#   ex 180 5000 10 600 
#  딕셔너리에 번호를 넣고, IN이면? OUT이면? + 그러면 누적합은 어떻게..
# 1)) 5961이면 KEY 5961 : [IN1,OUT1,IN2,OUT2...] 이렇게 한다음 FOR문 돌면서 짝수 - 홀수 해야겠다.

#  더 좋은 방법 없나..
#  2) 차 번호를 딕셔너리에 key로 등록하고 in이면 더하고, out이면 뺀다..
    dic = dict()
    for record in records :
        split = record.split(" ")
#       ex) [05:34,5961,IN]
#       시각을 분으로 환산하기
        split_time = split[0].split(":")
#       ["05","34"]
        total_minute = int(split_time[0])*60+int(split_time[1])
        
        if split[1] not in dic :
            dic[ split[1] ] = 0
        
        if split[2] == "IN" :
            dic[ split[1] ] -= total_minute
        
        else :
            dic[ split[1] ] += total_minute
#   하고 보니까 in만 했으면 out은 11:59니까 1439 더해주자..    
    for k,v in dic.items() :
        if v <= 0 :
            dic[k] += 1439
    
#   누적시간은 구했으니까 차량 번호순대로 정렬해놓고
    dic = sorted(dic.items(), key =lambda x:x[0])
    print(dic)
    
    time_list = []
    for i in range(len(dic)):
        time_list.append(dic[i][1])
        
#  요금 계싼
    answer = []
    for i in range(len(time_list)):
        fee = 0
        
        time_list[i] -= fees[0]
        
        if time_list[i] <= 0 :
            answer.append( fees[1])
            continue
        
        fee += fees[1]
        
        if time_list[i] % fees[2] == 0 :
            fee += (time_list[i] // fees[2]) * fees[3]
        else :
            fee += ((time_list[i] // fees[2]) + 1) * fees[3]
        answer.append(fee)
    
    return answer