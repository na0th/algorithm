def solution(s):
    
#   150000 = 10^5..
    go = s
    count_del_zero = 0
    count_trans = 0
    
    trans = []
    
    while len(go) >  1 :

        for item in go :
            if item == '1' :
                trans.append(item)
            else :
                count_del_zero+=1
           
        trans = ''.join(trans)

        go = str(bin(len(trans))[2:])
        
        trans = []
        count_trans+=1
    # print("count =",count)
    
    return [count_trans,count_del_zero]
        
        


   