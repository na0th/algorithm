import java.util.*;
class Solution {
    /**
    왼쪽->오른쪽으로 이동하다 '*'을 만나면 왼쪽을 제거한다라..

    알고리즘 분류 : for문 순회인가? -> 이전 것을 알아야한다.. 스택?
    어떻게 풀이
    1) '*'이 아니면 담는다
    2) '*'이면, 스택에서 1개 꺼낸다.

    3) 스택을 문자열로 만들어 리턴한다. 
     */
    public String removeStars(String s) {
        Deque<Character> st = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        for(char c : s.toCharArray()){
            if(c != '*'){
                st.addLast(c);
            }
            else{
                st.removeLast();
            }
        }
        if (st.isEmpty()){
            return "";
        }
        else {
            for(char c : st ){
                sb.append(c);
            }
        }
        return sb.toString();    
    }
}