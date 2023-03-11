def solution(phone_book):



#     아래의 함수 startswith 문자열 겹치는 거 체크하는 거 기억하기
#         if phone_book[i+1].startswith(phone_book[i]):

    
    # phone_book.sort(key = lambda x:x[0]) 이거는 안된다..
    # phone_book.sort()는 된다..     
    
#  정렬을 해놓으면 굳이 끝까지 뒤지지 않고 내 옆에만 비교하면 된다
#  ex 111,1189,235 이런 식으로 이미 아닌 게 나왔으면 앞으로 쭉 아니다 
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        count = 0
        str_len = len(phone_book[i])
        for j in range(str_len):
            if len(phone_book[i]) < len(phone_book[i+1]):
                if phone_book[i][j] == phone_book[i+1][j] :
                    count+=1
                else:
                    break
        if count == str_len :
            return False
    
    answer = True
    return answer
