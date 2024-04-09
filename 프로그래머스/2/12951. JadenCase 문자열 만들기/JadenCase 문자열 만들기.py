def solution(s):
#   공백을 기준으로 자르기+전체 소문자로 만들고+맨앞글자가 알파벳이면 대문자로..
    # s="  HI  HELLO"
    s = s.split(" ")
    s = [item.lower() for item in s]
    str = ""
    for item in s :
        if item =="":
            str+=" "
        else :
            str+=" "+item[0].upper()+item[1:]
    str = list(str)
    del str[0]
    a=""
    for item in str :
        if item =="":
            a+=" "
        else :
            a+=item
    return a
