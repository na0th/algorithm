import java.util.*;
class Solution {
    /**
    하위 시퀀스인지 확인해야 한다.
    abc , ahbgdc에서 abc가 ahbgdc중 불 필요한 걸 삭제하면 만들 수 있음..

    알고리즘 분류 : 투 포인터? 
    어떻게 풀이 ?
    각 문자열에 맨 왼쪽부터 시작해서, 서로 일치하면 포인터를 작은 문자열 거에서 1칸 오른쪽 옮김
    -> 큰 문자열도 1칸 옮긴다.
    서로 일치하지 않으면?
    -> 큰 문자열만 1칸 옮긴다.
     */
    public boolean isSubsequence(String s, String t) {
        int left = 0, right = 0;

        char[] wordS = s.toCharArray();
        char[] wordT = t.toCharArray();

        
        while(left<wordS.length && right<wordT.length ){
            
            if(wordS[left] == wordT[right]){
                left++;
            }
            right++;
        }
  

        return left == wordS.length;
    }
}