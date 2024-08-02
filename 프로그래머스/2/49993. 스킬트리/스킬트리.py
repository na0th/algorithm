def solution(skill, skill_trees):
    
    '''
    item in skil ? 해서 있으면 append 한다음 ''.join 해서 skil과 같으면 cnt +=1
    
    
    '''
    cnt = 0    
    
    from collections import deque
    skill_list = []
    for i in range(len(skill)):
        skill_list.append(skill[:i+1])
    skill_list.append("")
    # print(skill_list)
    for items in skill_trees : 
        result = deque()
        for item in items :        
            if item in skill :
                result.append(item)
        string = ''.join(result)
        
        # print(string)
#       C, CB , CBD 등이 가능하다..
        if string in skill_list :
            cnt +=1
    return cnt
    
    answer = -1
    return answer