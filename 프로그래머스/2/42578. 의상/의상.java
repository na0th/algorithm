import java.util.*;
class Solution {
    /*
    서로 다른 옷의 조합의 수 구하기
    
    알고리즘 분류 : 해시 맵
    
    어떻게 풀이?
    최소 1개의 의상은 입는다.
    1. map에 종류 갯수를 센다
    2. map에 있는 종류 갯수 전부 다 +1 해서 곱하고 -1 (의상을 아예 안 입는 경우는 없음)
    */
    public int solution(String[][] clothes) {
        Map<String, Integer> clothMap = new HashMap<>();
        
        for(String[] cloth : clothes){
            clothMap.put(cloth[1],clothMap.getOrDefault(cloth[1],0)+1);
            // if(!clothMap.containsKey(cloth[1])){
            //     clothMap.put(cloth[1],1);
            // }
            // else{
            //     clothMap.put(cloth[1],clothMap.get(cloth[1])+1);
            // }
             
            
        
        }
        
        int answer = 1;
        for (Integer value : clothMap.values()) {
            answer*=(value+1);
        }

        
        return answer-1;
    }
}
