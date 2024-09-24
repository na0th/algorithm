def solution(enroll, referral, seller, amount):
    from collections import defaultdict
    '''
    칫솔의 판매하면 10%를 추천인에게 배분, 나머지는 자신이 가짐
    추가로 자기 자식추천인에게서 발생의 10%까지 자신에 이익이 된다..
    
    10%는 원 단위에서 자르고, 10%가 1원 미만이면 이득을 분배하지 않고 자신이 가짐.
    
    enroll과 referral을 갖고 그래프를 만들어야 함(딕셔너리로 써보자)
    seller와 amount를 합쳐서 누가 칫솔 몇개를 팔았는지 확인
    
    딕셔너리에 value로 부모 노드를 갖고 있고, 종료 조건은 부모 노드 x or 10%가 1원 미만인 경우 중단
    
    '''
    dic = defaultdict(str)
    dic_amount = defaultdict(int)
    for i,item in enumerate(enroll) :
        dic[item] = referral[i]
        dic_amount[item] = 0
    # print(dic)
    # print(dic_amount)
    
    for i in range(len(amount)):
        amount[i] *= 100
        
    for person,num in zip(seller,amount):

#         while person != '-' and num >= 10:

#             dic_amount[person] += num - (num // 10)
#             num //= 10
#             person = dic[person]
            
#         dic_amount[person]+=num
        
        # 남은 금액이 10 미만이거나 더 이상 상위 조직원이 없는 경우
        # dic_amount[person] += num
        while (person != '-') :
            # if 10%가 1원 미만이면 -> 내가 10원 미만이면 안 나누고 다 내가 가짐 :
            if num < 10 :
                dic_amount[person] += num
                break

            #지금 나한테 90%를 줌
            dic_amount[person]+= num  - (num//10)
            num //= 10 

            #타고 타고 올라가면서 분배..
            person = dic[person]

            

    
    result = list(dic_amount.values())
    # result = [dic_amount[item] for item in enroll]
    return result

    
        
    
