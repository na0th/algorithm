import java.util.*;
class Solution {
    /*
    폰켓몬..
    N마리중 N/2마리를 가져가도 좋다..
    폰켓몬은 종류에 따라 번호가 붙여져있음
    [3,1,2,3]이라면 2마리를 골라야 하니 서로 다른 폰켓몬 종류를 고른 최대가 2개.. 
    이렇게 최대한 다양한 종류를 골랐을 때, 최대값 구하시오
    
    항상 짝수 ..
    
    알고리즘 분류 : 해시,정렬? 
    어떻게 풀이?
    해시로 카운팅 한 후 정렬해서 N/2를 넘어가는 CNT를 세기? 
    */
    public int solution(int[] nums) {
        Map<Integer,Integer> numMap = new HashMap<>();
        
        for(int num : nums){
            numMap.compute(num, (k,v) -> v == null ? 1 : v + 1);
        }
        
        int uniqueCount = numMap.size();        
        int maxPick = nums.length / 2;         
        
        return Math.min(uniqueCount, maxPick);

    }
}