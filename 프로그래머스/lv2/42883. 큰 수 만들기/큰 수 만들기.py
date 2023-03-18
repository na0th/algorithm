def solution(number, k):
#   맨 처음부터 내가 뒤 숫자보다 작으면 삭제 
#   삭제한 후에는 처음부터 다시 돈다
#   k개 삭제하면 break 
    
    cursor = 0
    while cursor < len(number)-1 and k > 0:
        
        if number[cursor] < number[cursor+1]:
            number =  number[:cursor] + number[cursor+1:]
            k-=1
            if cursor > 0 :
                cursor-=2
            else :
                cursor-=1
        
        cursor+=1
        
        
    if k > 0  :
        return number[:len(number)-k]
            
    return number
    