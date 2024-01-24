def solution(book_time):
#   딕셔너리에 등록?
#   종료 시각 ex)15:20 을 : 기준으로 split 해서 split[0]*60 + split[1]+10을 저장함
#   room_list = [920,1040]
#   book_time의 item만큼 돌면서 room_list의 element중 내 시작시간보다 작은 게 있다면 바꿔

#   시작 시간으로 정렬..
    book_time = sorted(book_time,key = lambda x:x[0])
    
    room_list = []
    for time in book_time :
        time_start = time[0].split(":")
        start_minute = int(time_start[0]) * 60 + int(time_start[1])
        
        time_split = time[1].split(":")
        time_hour = int(time_split[0]) * 60
        time_minute = int(time_split[1])
        
        time_to_minute = time_hour+time_minute
        
#       맨 처음에 값을 넣어줘야 하는데..
        if not room_list :
            room_list.append(time_to_minute + 10)
            continue
        if start_minute < min(room_list):
            room_list.append(time_to_minute + 10)
        else :
            idx = room_list.index(min(room_list))
            room_list[idx] = time_to_minute + 10

    answer = len(room_list)
    return answer