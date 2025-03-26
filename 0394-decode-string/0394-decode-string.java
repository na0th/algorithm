import java.util.*;
class Solution {
    /**
    괄호안의 문자를 맨 앞 숫자가 곱하는 구조

    알고리즘 분류 : 스택
    어떻게 풀이?
    1)string 1글자를 읽는다
    숫자, [ , ], 문자 구분
    숫자는 숫자 배열
    [은 추가
    문자는 문자 배열
    ]은 빼기

    ex)) 3[a2[c]]
    nums=[3,2]
    strs=["",a,"",c]
    string = ""
    1) 3은 숫자 배열에 추가
    2) [는 문자 배열에 빈 문자 "" 추가
    3) a는 문자 배열에 추가
    4) 2는 숫자 배열에 추가
    5) [는 문자 배열에 빈 문자 "" 추가
    6) c는 문자 배열에 추가
    7) ]는 문자 배열에서 문자 1개 빼서 숫자만큼 곱해서 문자 배열에 있는 문자 교체
    8) ]는 문자 배열에서 문자 1개 빼서 숫자만큼 곱해서 문자 배열에 있는 문자 교체

    7번부터 ]를 뽑았으니 c를 숫자 2를 곱해 cc로 만든 다음
    ""를 더하고 strs의 c를 cc로 교체하고 숫자 배열에서는 삭제
      
    
    */
    public String decodeString(String s) {
        Deque<Integer> numSt = new ArrayDeque<>();
        Deque<String> strSt = new ArrayDeque<>();
        String curString = "";
        int num = 0;
        for(char ch :s.toCharArray()){
            if(Character.isDigit(ch)){
                num = num * 10 + ch-'0'; 
                // 숫자가 꼭 한 자리는 아닐 수 있으니까.. 
            }else if(ch == '['){
                numSt.addFirst(num);
                strSt.addFirst(curString);
                num = 0;
                curString = "";
            }else if(ch == ']'){
                int repeat = numSt.removeFirst();
                String prev = strSt.removeFirst();
                curString = prev + curString.repeat(repeat);
            }else{
                curString += ch;
            }
        }


    return curString;
    }
}