import java.util.*;

class Solution {
    /**
    1231
    1231

    01231
    01244

    027931
    0 2 7 11 11 12
    2칸까지는 확정 (첫번쨰 값? 두번째 값?)
    그다음 왼쪽에서 바로 올래? 아니면 2번째 전 값 + 나 ?

    알고리즘 분류 : dp
    어떻게 풀이? 
    max(dp[i-1],dp[i-2]+nums[i])

    */
    public int rob(int[] nums) {
        
        // Deque<Integer> deque = new ArrayDeque<>(Arrays.stream(nums)
        //     .boxed()
        //     .collect(Collectors.toList()));
        // deque.addFirst(0);
        // System.out.println(deque);
        
        Map<Integer,Integer> dp = new HashMap<>();
        

        if (nums.length==1) return nums[0];
        dp.put(0,0);
        dp.put(1,nums[0]);
        for (int i = 2; i <= nums.length; i++) {
            dp.put(i, Math.max(dp.get(i - 2) + nums[i - 1], dp.get(i - 1)));
        }
        return dp.get(nums.length); 
    }
}