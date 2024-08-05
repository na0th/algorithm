def solution(files):


#       '''
#       1. head number tail 자르기
#       2. head 사전순 정렬(대소문자 구분 X) , 같을 경우 Number 숫자 순으로 정렬, 숫자앞0 없앰
#       3. head, number 다 같으면 들어온 순서대로..


#       '''
    final = []
    for i , file in enumerate(files) :
        head = []
        number = []
        tail = []
        check1 = True
        check2 = False
        check3 = False
        for item in file :
            # print(item)
            if check1 == True and item.isdecimal() :
                check1 = False
                check2 = True
            if check2 == True and not item.isdecimal() :
                check2 = False
                check3 = True
            if  check1 == True and (item.isalpha() or item in (' ','-','.')) :
                if item.isalpha() :
                    item = item.upper()
                head.append(item)   
            elif check2 == True and item.isdecimal() : 
                number.append(item)
            elif check3 == True :
                if item.isalpha() :
                    item = item.upper()
                tail.append(item)
        head = ''.join(head)
        number = ''.join(number)
        tail = ''.join(tail)
  
        final.append([i,head,number,tail])
    final.sort(key =lambda x: (x[1],int(x[2]),x[0]))
    

    result = []
    for item in final :
        
        result.append(files[item[0]])
        
    return result
    