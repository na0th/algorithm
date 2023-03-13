def solution(word):
#   순열 써서 다 만든 다음에 정렬해서 인덱스 리턴하면 되나?
#   근데 중복이 포함되어야 한다. -> 중복 순열
    import itertools
    list1 = []
    sets=['A','E','I','O','U']
    for i in range(1,6):
        data = list(itertools.product(sets,repeat=i))
        list1.extend(data)
 
    list2=[]
    for sett in list1 :
        a = [*sett]
        text = ''.join(a)
        list2.append(text)
    list2.sort()
# list2에서 그냥 word 인덱스 찾자..
    answer=list2.index(word)+1

        
        

   
    return answer