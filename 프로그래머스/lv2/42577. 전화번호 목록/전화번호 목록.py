def solution(phone_book):
    
#     phone_book.sort()

#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False

#     return True
    
    # phone_book.sort(key = lambda x:x[0])
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