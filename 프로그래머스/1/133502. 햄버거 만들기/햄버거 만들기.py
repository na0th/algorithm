def solution(ingredient):
#   상수의 앞에 아래서부터 위로 쌓이고 
#  빵 야채 고기 빵으로 쌓인 햄버거만 포장

# 슬라이싱해볼까..? 아닌 듯..

#   01234 1번까지 가능 이니까 for i in range(2)

#    123 /1231/ 1 이면 1231이 빠지니까 123 /1231/ 1이 1231이 되어 2번임..

#   stack 활용?

        
        
#    st안에 3개도 없으면 그냥 push 후에 continue .. st < 3
#    st안에 3개가 있다면 st[-1:-4] + ingredient(i) 가 1231이면 다 pop
    
    i,cnt,st = 0,0,[]
    
    for i in ingredient:
        st.append(i)
        
        if (st[-4:]) == [1,2,3,1] :
            del st[-4:]
            cnt+=1

    return cnt
    