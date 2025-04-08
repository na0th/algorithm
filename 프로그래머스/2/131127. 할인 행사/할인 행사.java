import java.util.*;
class Solution {
    /**
    알고리즘 분류 : 해시 
    어떻게 풀이?
    1.첫날부터 number.size일 동안의 할인 목록을 구함
    2. 일치하면 +1 
    
    */
    public int solution(String[] want, int[] number, String[] discount) {
        int n = number.length;
        int days = discount.length;
        int answer = 0;
        Map<String,Integer> wantMap = new HashMap<>();
        
        for(int i=0; i<want.length; i++){
            wantMap.put(want[i],number[i]);
        }
        
        for(int i =0; i<days-9; i++){
            Map<String, Integer> curDiscount = new HashMap<>();
            
            //해당 일에 회원가입하면 10일동안의 할인 메뉴 모음
            for(int j=i; j<i+10; j++){
                if(!curDiscount.containsKey(discount[j])){
                    curDiscount.put(discount[j],1);
                }
                else{
                    curDiscount.put(discount[j],curDiscount.get(discount[j])+1);
                }
                    
            }
            
            if(wantMap.equals(curDiscount)){
                answer++;
            }
        }
        
        
        return answer;
    }
}