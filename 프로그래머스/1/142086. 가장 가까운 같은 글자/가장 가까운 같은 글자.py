def solution(s):
#   나왔나 안 나왔나는 딕셔너리로 하자
#   가장 가까운 글자는 인덱스를 써야하는데.. 리스트랑 딕셔너리 같이?
#   처음에 딕셔너리에 저장하면서 인덱스를 같이 저장한다(a:[1,3,5]) 이런 식으로
#   그리고 a를 찾아가서 
    # from collections import defaultdict
    # dic = defaultdict(list)
    # for item in s :
    #     if item not in dic :
    #         dic[item].append()
    # print(dic)
#     from collections import defaultdict
#     dic = defaultdict(list)
    dic = {}
    s = list(s)
    for idx,item in enumerate(s):
        if item not in dic :
            dic[item]=[idx]
        else :
            dic[item].append(idx)
            
    print(dic)

    answer = []
    for i in range(len(s)):
        if i == dic[s[i]][0] :
            answer.append(-1)
        else :
            index = dic[s[i]].index(i)
            answer.append((dic[s[i]][index]-dic[s[i]][index-1]))
            # answer.append((dic[s[i]]-dic[s[i-1]]))


                          
    print(answer)
    return answer