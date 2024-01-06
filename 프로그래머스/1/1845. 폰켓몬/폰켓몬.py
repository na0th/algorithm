def solution(nums):
#  시간 복잡도는 n^2이하로 생각해보자..
#     그냥 딱 드는 생각 counter 함수로 카운팅한 k,v로 딕셔너리를 활용하자
#  예를 들어 n/2 보다 카운팅된 k,v쌍이 적다면 ? , 많으면 그냥 n/2를 리턴..
#  적다면 전체 k,v쌍을 리턴하면 되겠구나..

    from collections import Counter
    
    dict = Counter(nums)
    
    if len(dict) >= (len(nums) / 2) :
        return (len(nums) / 2)
    else :
        return len(dict)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
#     무조건 짝수인가? n/2마리니까..
#   그냥 dic에 넣어서 n/2보다 종류가 많으면? n/2 리턴
#  n/2보다 종류가 적으면? 그 종류 리턴

#     dic={}
#     for i in range(len(nums)):
#         if nums[i] not in dic:
#             dic[nums[i]] = 1
#     if len(dic) >= len(nums) / 2 :
#         answer = len(nums) / 2
#     else :
#         answer = len(dic)
    
#     return answer