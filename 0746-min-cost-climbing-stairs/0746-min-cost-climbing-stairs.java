import java.util.*;

class Solution {
    /**
    인덱스 0 or 1 시작
    계단을 1개 or 2개를 올라갈 수 있습니다.
    최소 비용을 반환하기

    알고리즘 분류 : DP
    어떻게 풀이 ? 
    인덱스 0에서 시작하는 경우
    인덱스 1에서 시작하는 경우
    
    두 경우로 나눠서, COST[I]= MIN( COST[I-2]+누적, COST[I-1]+누적)
    한 칸 전에서 올라온 경우와, 두 칸 전에서 올라온 경우중 최소를 구한다.

     */
    public int minCostClimbingStairs(int[] cost) {
        Map<Integer,Integer> dp1 = new HashMap<>();
       dp1.put(0,cost[0]);
       dp1.put(1,cost[1]);

       for(int i=2; i<cost.length; i++){
            int value = Math.min(dp1.get(i-1),dp1.get(i-2))+cost[i];
            dp1.put(i,value);
       }
       int n = cost.length;
       return Math.min(dp1.get(n-1),dp1.get(n-2));
    }
}