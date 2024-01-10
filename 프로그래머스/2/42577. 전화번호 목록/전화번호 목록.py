def solution(phone_book):
    
#    시간복잡도 n^2은 안된다.. nlogn 애매.. n 괜찮음..

#  딕셔너리에 전부 등록한 후에.. ??  = 모르겠다.....

#  문자열이라 정렬해서.. 이렇게 되겠지? 12,123,1235,567,88 ... 
#  119 1191 1201 ,, len이 작을 때만
   
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]) :
            cnt = 0
            for j in range(len(phone_book[i])):
                if phone_book[i][j] == phone_book[i+1][j] :
                    cnt+=1
            if cnt == len(phone_book[i]) :
                return False
    return True


    
    
    
    
    
    
    
    
    
    # dic={'abc':'1','bfced':'1'}
    # if 'abc' in dic :
    #     print("있음")
    # answer=True
#     answer = True
#     hash_map = {}
# #   해시 맵에 저장
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
        
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
            
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return answer

    