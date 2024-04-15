def solution(ingredient):
#   상수의 앞에 아래서부터 위로 쌓이고 
#  빵 야채 고기 빵으로 쌓인 햄버거만 포장

# 슬라이싱해볼까..? 아닌 듯..

#   01234 1번까지 가능 이니까 for i in range(2)

#    123 /1231/ 1 이면 1231이 빠지니까 123 /1231/ 1이 1231이 되어 2번임..

#   stack 활용?

    # cnt = 0 
    # for i in range(len(ingredient)-3):
    #     if ingredient[i:i+3] == [1,3,2,1] :
    #         cnt+=1
    # return cnt
        
        
#    st안에 3개도 없으면 그냥 push 후에 continue .. st < 3
#    st안에 3개가 있다면 st[-1:-4] + ingredient(i) 가 1231이면 다 pop
    
    i,cnt,st = 0,0,[]
    
    while(i<len(ingredient)):
        if len(st) < 3 :
            st.append(ingredient[i])
        else :
            
            # print(st[-3:]+[ingredient[i]])
            if (st[-3:]+[ingredient[i]]) == [1,2,3,1] :
                cnt+=1
                del st[-3:]
                i+=1
                continue
            else:
                st.append(ingredient[i])
        i+=1
    return cnt
    # print(st)