import java.util.*;

class Solution {
    /**
    같은 형태가 반복되는 덧셈
    알고리즘 분류 : dp
    어떻게 풀이?
    dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
     */
    public int tribonacci(int n) {
        Map<Integer, Integer> dp = new HashMap<>();

        dp.put(0,0);
        dp.put(1,1);
        dp.put(2,1);

        if(n == 0){
            return 0;
        }
        if(n==1 || n ==2){
            return 1;
        }


         
        for(int i= 3; i<n+2; i++){
            int num = dp.get(i-1) + dp.get(i-2) + dp.get(i-3);
            dp.put(i,num);
        }    
        // for(int num : dp.values()){
        //     System.out.println(num);
        // }
        return dp.get(n);
    }
}