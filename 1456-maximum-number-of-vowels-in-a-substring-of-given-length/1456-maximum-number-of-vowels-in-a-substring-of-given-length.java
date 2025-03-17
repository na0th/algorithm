import java.util.*;
class Solution {
    /**
    문자열중 길이가 k인 부분 문자열에서 모음의 최대 갯수 반환
    알고리즘 분류 : 슬라이딩 윈도우
    어떻게 풀이?
    --- 
     ---
    위의 방식대로 왼쪽거를 제거하고, 오른쪽것만 더하면서 해나감..
    몇번? n-k+1번..
    123
     123
      123 
       123
        123
    7은 길이 3이 5번 이동..
     */
    public int maxVowels(String s, int k) {
        Map<Character,Integer> map = new HashMap<>();
        map.put('a',1);
        map.put('e',1);
        map.put('i',1);
        map.put('o',1);
        map.put('u',1);

        int maxCount = 0;
        int curCount = 0;

        for (int i = 0; i < k; i++) {
            if (map.containsKey(s.charAt(i))) {
                curCount++;
            }
        }
        maxCount = curCount;  // 초기 값 저장
        for(int i=k; i<s.length();i++){
            
            if(map.containsKey(s.charAt(i))){
                curCount++;
            }
            if(map.containsKey(s.charAt(i-k))){
                curCount--;
            }
            maxCount = Math.max(maxCount, curCount);
           
        }
        return maxCount;
    }
}