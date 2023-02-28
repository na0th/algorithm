def solution(nums):
#     무조건 짝수인가? n/2마리니까..
#   그냥 dic에 넣어서 n/2보다 종류가 많으면? n/2 리턴
#  n/2보다 종류가 적으면? 그 종류 리턴

    dic={}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
    if len(dic) >= len(nums) / 2 :
        answer = len(nums) / 2
    else :
        answer = len(dic)
    
    return answer