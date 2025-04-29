import java.util.*;

class Solution {
    /*
    단 1명 빼고 다 완주함
    명단, 완주 명단이 주어졌을 떄, 완주하지 못한 참가자의 이름을 return
    
    알고리즘 분류 : 해시
    
    어떻게 풀이? 
    1)참가자를 key : 1(+1) 꼴로 저장
    2)completion에 있으면 key 찾아서 -1
    리턴
    
    
    */
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> map = new HashMap<>();
        
        for(String p : participant){
            if(!map.containsKey(p)){
                map.put(p,1);
            }else{
                map.put(p,map.get(p)+1);
            }
        }
        
        for(String s : completion){
            if(map.containsKey(s)){
                map.put(s,map.get(s)-1);
            }
        }
//         for(String s : map.keySet()){
//             System.out.println(s);
//         }
//         System.out.println(map.values());
        
//         for(Map.Entry<String,Integer> entry : map.entrySet()){
//             System.out.println(entry.getKey()+entry.getValue());
//         }
        
        String answer = null;
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == 1) {
                answer = entry.getKey(); // value가 1인 key 반환
            }
        }
        return answer;
    }
}