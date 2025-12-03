import java.util.*;
class Solution {
    /*
    분류 : 해시 
    고려할 점  : 동명이인이 있다. A가 2명있으면 1명만 들어왔으면 A가 완주하지 못한 것
    어떻게 풀이? 
    1. participant를 해시에 등록
    2. completion을 순회하면서 해시에 등록됐는지 확인
    
    */
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>();
        for(String parti : participant){
            map.put(parti, map.getOrDefault(parti,0)+1);
        }
        for(String compl : completion){
            map.put(compl, map.get(compl)-1);
        }
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue() == 1){
                answer = entry.getKey();
            }
        }
        return answer;
    }
}