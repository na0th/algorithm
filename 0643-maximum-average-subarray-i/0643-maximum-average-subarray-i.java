import java.util.*;
class Solution {
    /**
    k개의 연속 값의 평균을 구하고, 최대 값을 구합니다.
    알고리즘 분류 : 구현? 순회?
    어떻게 풀이?
    for문을 돌면서 k개의 값을 더한다. (n-k번 인덱스까지)
    평균을 구하고, 최대값을 구한다

    
    */
    public double findMaxAverage(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        for(int i=0; i<nums.length-k+1;i++){
            int temp = 0;
            for(int j=0; j<k; j++){
                temp += nums[i+j];
            }
            if (max < temp){
                max = temp;
            }
        }    
        return  (double) max / k;
    }
}