import java.util.*;
class Solution {
    /** 
    왼쪽과 오른쪽을 나눠서 곱하자.

    0/ 2~4
    234

    1~2/3~4 
    134

    1~2/4~
    124

    1~3/ 
    123

    1*(1) 1*(2) 12*(3) 123*(4)
    
    알고리즘 분류 : dp?
    어떻게 풀이 ? 

    나(인덱스)를 기준으로 왼쪽 곱 * 오른쪽 곱 
    즉, 내가 6이면 왼쪽곱 2 * 오른쪽곱 4를 하면 8이 된다. 

    범위를 벗어나는 값이라면 1을 곱하면 된다.
    1  2  6  24
    24 24 12 4


     */
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int[] leftArr = new int[size];
        int[] rightArr = new int[size];
        int[] resultArr = new int[size];

        leftArr[0] =nums[0];
        rightArr[size-1] = nums[size-1];

        for(int i=1; i< size; i++){
            leftArr[i] = nums[i]*leftArr[i-1];
        }
        for(int i=size-2; i>0 ; i--){
            rightArr[i] = nums[i]*rightArr[i+1];
        }

        for (int i = 0; i < size; i++) {
            if (i == 0) {
                resultArr[i] = rightArr[i + 1];
            } else if (i == size - 1) {
                resultArr[i] = leftArr[i - 1];
            } else {
                resultArr[i] = leftArr[i - 1] * rightArr[i + 1];
            }
        }
        return resultArr;
    }
}