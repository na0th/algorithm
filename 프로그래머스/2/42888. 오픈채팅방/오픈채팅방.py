def solution(record):
  # 닉네임 변경 2가지 방법 
# '''
# 닉네임 변경은 2가지 방법이 있다.
#     1.채팅방을 나간 후 새로운 닉네임
#     2.채팅방에서 닉네임 변경
    
#     .. 나갈 때는 기존 닉네임도 변경한 닉네임으로 다 바뀜
    
#     최종 문자열 배열을 리턴
#     n은 10^5
#     시간 복잡도 n^2이하 nlogn부터 가능
    
#     메세지는 
#     1.입장 ex) Enter uid1234 Muzi
#     2.변경 ex) Change uid1234 Muzi
#     3.퇴장 ex) Leave uid1234
    
#      해시 등록만 해놓자..
#      uid1234: Muzi
# '''
    result = []
    dic = {}
    for item in record :
        word_list = item.split(" ")
        if word_list[0] == 'Enter':
            dic[word_list[1]] = word_list[2]
            result.append("님이 들어왔습니다.")
        elif word_list[0] == 'Leave':
            result.append("님이 나갔습니다.")
        elif word_list[0] == 'Change':
            dic[word_list[1]] = word_list[2]
        
#         print(word_list)
#         print(dic)
    add_list = []
    for item in record :
        word_list = item.split(" ")
        if word_list[0] != 'Change':
            add_list.append(dic[word_list[1]]) 
            
    for i in range(len(result)):
        result[i] = add_list[i]+result[i]
    # print(add_list)
    
    return result