def solution(s):
#     0...n-1 이동까지 총 n번 회전..
#     올바른 괄호인지는 스택을 통해서 반대편이 나오면 pop 시킨다...
#     끝까지가서 빈 스택이 되면! 그건 올바른 괄호..
    
     
    cnt = 0   
    for i in range(len(s)):
        
        a = s[i:]+s[:i]
 
        st = []
        k = 0 

        while(k < len(a)):

            if not st :
                st.append(a[k])

    #       st은 있고, 뒤집어서 나랑 같으면 안에 있는 애를 pop하기..
            elif st and (st[-1] == '[' and a[k] == ']'):
                st.pop()
            elif st and (st[-1] == '{' and a[k] == '}'):
                st.pop()
            elif st and (st[-1] == '(' and a[k] == ')'):
                st.pop()

            elif st[-1] == '[' and a[k] == ('}' or ')') :
                break
            elif st[-1] == '(' and a[k] == (']' or '}') :
                break
            elif st[-1] == '{' and a[k] == (']' or')') :
                break
            else:
                st.append(a[k])
            k+=1

        if not st :
            cnt+=1
    return cnt
    

