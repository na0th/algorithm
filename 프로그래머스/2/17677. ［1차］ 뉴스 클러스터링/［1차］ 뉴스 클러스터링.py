def solution(str1, str2):
    from collections import Counter
#   2글자씩 자르기 + 알파벳(2글자) 아니면 추가 X
    def func(str):
        list = []
        for i in range(len(str)-1):
            if str[i:i+2].isalpha() :
                list.append(str[i:i+2])    
        return list
    
    
    def func2(list):
        list = [item.lower() for item in list]
        return list
        
    list1 = func(str1)
    list1 = func2(list1)
    
    list2 = func(str2)
    list2 = func2(list2)
    
    print("list1 = ",list1,"list2 = ",list2)
#   교집합 , 합집합 구하기 (두 집합이 빈 집합이면 1 리턴)
    if not list1 and not list2:
        return 65536
    else :
        dic1 = Counter(list1)
        dic2 = Counter(list2)
        
        uni_list = set(list1).union(set(list2))
        
        inter = 0
        uni = 0
        
        for item in uni_list :
        #둘 다 있다. 작은 애는 교집합으로, 큰 애는 합집합으로.. 추가
            if item in dic1 and item in dic2 :
                if dic1[item] >= dic2[item] :
                    uni += dic1[item]
                    inter += dic2[item]
                else :
                    uni += dic2[item]
                    inter += dic1[item]
            #list1에만 있다 .
            if item in dic1 and item not in dic2 :
                uni += dic1[item]
            #list2에만 있다.      
            if item not in dic1 and item in dic2:
                uni += dic2[item]

        return int((inter/uni)*65536)

    
#   다 소문자 취급하기 
    # map를 활용한 변환 
    
    # c = list(map(lambda x:x.lower(),a))   
    # print(c)
    
    # a = [item.lower() for item in a]
    # print(a)
    
    