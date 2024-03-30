def solution(msg):
#   알파벳 담은 딕셔너리 + number 변수 
    answer = []
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    number = 26
    
    i = 0
    while(i <= len(msg)) :
        
        for k in range(i+1,len(msg)+1) :
            if msg[i:k] in dic :
                if k == len(msg):
                    answer.append(dic[msg[i:k]])
                    return answer
                continue
            else :
                number+=1
                dic[msg[i:k]] = number
                # print("=",dic[msg[i:k-1]])
                answer.append(dic[msg[i:k-1]])
                break
        # print(i,k)
        i += len(msg[i:k-1])
        # print(i,k)

    return answer