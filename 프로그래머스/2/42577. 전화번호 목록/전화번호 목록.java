import java.io.*;
import java.util.*;
class Solution {
    /*
    전화 번호의 접두어가 있는지 확인해야 한다.
    알고리즘 분류 : 해시
    어떻게 풀이? 
    각 전화번호마다 돌면서 1글자씩 더해가며 Map에 있는지 확인한다.
    */
    public boolean solution(String[] phone_book) {
        HashMap<String, Integer> map = new HashMap<>();
        for(String phoneNumber : phone_book){
            map.put(phoneNumber,1);
        }
        for(Map.Entry<String,Integer> entry : map.entrySet()){
            StringBuilder sb = new StringBuilder();
            String phoneNumber = entry.getKey();
            for(char phoneNum : phoneNumber.toCharArray()){
                sb.append(phoneNum);
                
                if(map.containsKey(sb.toString()) && !sb.toString().equals(phoneNumber)){
                    return false;
                }
                // System.out.println(sb);
            }
            sb.setLength(0);
            
            // System.out.println(entry.getKey()+" "+entry.getValue());
        }
        
        return true;
    }
}