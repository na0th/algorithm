import java.util.*;
class Solution {
    
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        
        for(String comp : completion){
            map.put(comp,map.getOrDefault(comp,0)+1);
        }
        // System.out.println(map.toString());
        
        String answer = "";
        for(String parti : participant){
            if(map.containsKey(parti)){
                map.put(parti,map.get(parti)-1);
            }
            else{
                answer = parti;
            }
        }
        
        
        for(Map.Entry<String,Integer> entry : map.entrySet()){
            if(entry.getValue()==-1){
                answer = entry.getKey();
            }
        }
        
        return answer;
    }
}
