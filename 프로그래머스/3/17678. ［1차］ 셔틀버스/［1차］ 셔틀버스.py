def solution(n, t, m, timetable):
    from collections import Counter
    '''
    09시부터 n회 t분 간격 최대 m명
    09:00에 줄을 서도 09시 버스 탑승 가능
    
    콘은 셔틀 대기열 같은 시각 도착한 크루 중 제일 뒤에 선다
    모든 크루는 23:59에 집에 가서 다음 날 셔틀 타는 일 없다.
    
    콘이 몇등이 되어야 하는가?
    9시 시작이고 .. n회 m명 t분 간격..
    
    예제 1번 9시부터 1회 1분간격 5명씩
    timetable중 총 태울 수 있는 인원은 4명
    나는 4등 해도 됨 vs 9시 비교
    
    
    
    예제 2번 9시부터 2회 10분간격 2명씩
    timetable중 총 태울 수 있는 인원은 3명
    나는 3등하면 됨
    
    예제 3번 9시부터 2회 1분 간격 2명씩
    총 태울 수 있는 인원은 4명
    나는 4등하면 됨(완전히 꽉 찬 n*m이야 그러면 -1분)


    예제 4번 9시부터 1회 1분 간격 5명씩, 실 탑승자 지금 5명차지
    나는 timetable에서 5등해도 됨 근데 완전히 꽉찬 n*m이야 그러면 -1분
    
    예제 5번 9시부터 1회 1분 간격 1명씩, 실 탑승자 지금 0명 가능
    나는 timetable중에서 1등하면 됨 = 막차타자

    예제 6번,9시부터 10회 60분 간격 45명씩, 실 탑승자 지금 0명 가능
    나는 tiimetable중에서 1등하면 됨 = 막차타자
    
    
    
    막차 전까지는 대기열에서 사람들을 내보냅니다. 현재 시각을 갱신합니다.

    막차 시간에 대기열에서 탑승 가능한 사람이
    정원(m) 이상이라면, 탑승 가능한 마지막 사람보다 1분 전에 탑승합니다.
    정원보다 작다면, 현재 시간(=막차시간)에 탑승합니다.
    '''
    def trans(minute) :
        string = ""
        h = minute//60
        m = minute % 60
        if h < 10 :
            string+="0"+str(h)
        else :
            string+=str(h)
        string+=":"
        if m < 10 :
            string +="0"+str(m)
        else :
            string+=str(m)
        return string
    
#   실 탑승자를 구해..
    t_list = []
    for time in timetable :
        temp = time.split(":")
        minute = int(temp[0])*60 + int(temp[1])
        t_list.append(minute)
    t_list.sort(reverse=True)
    print(t_list)
    
    s_time = 540
    for i in range(n-1):
        cnt = 0
        while(cnt < m and t_list) :
            if t_list[-1] <= s_time :
                t_list.pop()
            cnt+=1
        s_time+=t
#   마지막 차를 탈 때
    counter = Counter(t_list)
    
    counter = dict(sorted(counter.items() , key=lambda x : x[0]))
    print(counter)
    
    count = 0
    for k,v in counter.items():
        if k <= s_time:
            count+=v
    
    print(count)
    if count>= m :
        last_count = 0
        for k,v in counter.items() :
            if last_count + v >= m :          
                return trans(k-1)
            else :
                last_count+=v
#       탑승 가능한 마지막 사람보다 -1분
    else :
        return trans(s_time)
        
    print(t_list)
    
   
    
    