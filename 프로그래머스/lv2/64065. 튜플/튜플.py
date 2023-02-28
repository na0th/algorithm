def solution(s) :
    s=s.replace("{","")
    s=s.replace("}","")
    s=s.split(",")

    dic={}
    for i in range(len(s)):
        if s[i] not in dic :
            dic[s[i]] = 1
        else :
            dic[s[i]] +=1  
    list1=sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(list1)
    answer=[]
    for i in range(len(list1)):
        answer.append(int(list1[i][0]))
    
    return answer