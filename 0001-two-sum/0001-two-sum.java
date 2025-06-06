import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            map.put(target-nums[i],i);
        }
        System.out.println(map.toString());

        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])  && map.get(nums[i]) != i ){

                if(i>= map.get(nums[i])){
                    return new int[] {map.get(nums[i]),i};
                }
                else{
                    return new int[] {i,map.get(nums[i])};
                }
                
            }
        }
        return new int[] {};
    }
}