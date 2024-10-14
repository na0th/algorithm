def solution(cards):
    from collections import Counter
#     카드 100장이 있다.. 숫자 2~100중 하나를 정하고
#  그 수보다 작거나 같은 숫자카드를 준비해서 , 준비한 카드의 수만큼 작은 상자 준비
#  10을 정하면, 1~10까지 카드 10개, 상자 10개 상자에 카드를 넣고 무작위 나열
#  하나를 선택해서 숫자카드 확인, 그 상자로 가서 확인한다..
#  1번 상자에서 4를 택, 4에서 7을 택 7에서 1을 택 .. 그럼 그만.. 1번 그룹 
#  2번 그룹은 1번 상자그룹을 뺀 후 랜덤으로 뽑아서 똑같이 이미 열려있을 때까지..

#  그래프로 묶기.. 해야 함.
    '''
    리턴 : 사이클끼리 묶어서 원소의 개수가 가장 큰 2개의 사이클을 곱해라..
    
    예외) 1번 상자 그룹으로 끝나면 점수는0 점
    
    어떻게 .. ?
    union find?
    
    union find 해놓고 부모를 기준으로 Counter하면 부모가 똑같은 원소 많은 부모 2개 나옴. 그거 곱하기
    부모 1개다? 그럼 return 0
    '''
    
    parent = [i for i in range(len(cards))]
    # print(parent)


    def find_parent(parent,x):
        if parent[x] != x :
            parent[x] = find_parent(parent,parent[x])
            #나랑 내 부모랑 같으면 걔는 부모 노드
        return parent[x]
    
    def union_parent(parant,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)

        # if a < b :
        #     parent[b] = a
        # else :
        #     parent[a] = b
        if a != b:
            parent[b] = a
    
    for i in range(len(cards)):
        # print("before",i,parent)
        next_box = cards[i]-1

        union_parent(parent,i,next_box)
        # print("before",parent)
    for i in range(len(parent)):
        find_parent(parent, i)
        
    count_dict = Counter(parent)
    v = list(count_dict.values())
    if len(v) == 1:
        return 0
    else :
        v.sort(reverse=True)
        return v[0]*v[1]
    
    

    