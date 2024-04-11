def solution(s):
    answer = -1

    st = []
    i = 0
    while(i < len(s)):
        if not st or st and st[-1] != s[i] :
            st.append(s[i])
            i+=1 
            continue
        elif st and st[-1] == s[i]  :
            st.pop()
            i+=1

    

    return 0 if st else 1