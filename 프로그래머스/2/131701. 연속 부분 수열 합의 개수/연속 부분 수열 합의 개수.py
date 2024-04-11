def solution(elements):
    len_num=len(elements)
    elements = elements*2
    print(elements)
    
    dict = {}
    for num in range(0,len_num):
        for i in range(len_num):
            # print(elements[i:i+num+1])
            # print(sum(elements[i:i+num+1]))
            if sum(elements[i:i+num+1]) not in dict :
                dict[sum(elements[i:i+num+1])]=1
    # print(dict)
    # print(len(dict))
        
    return len(dict)