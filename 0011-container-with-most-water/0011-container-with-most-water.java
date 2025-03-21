import java.util.*;
class Solution {
    /**
    용기가 저장할 수 있는 최대 물의 양을 반환
    용기가 되려면.. a~b까지이고 min(height[a], height[b]) * (b-a)인데...
    많은 경우의 수가 있지만 n이 10^5인 걸 보면, O(N^2)은 안될 것 같다..
    최적화하려면 투포인터 쓰자

    알고리즘 분류 : 투포인터(2중 FOR문으로는 시간 초과)
    어떻게 풀이?
    꼭 맨 오른쪽이 최고가 아니다!
    포인터를 이동하는 방식?? 
    -> 높이가 낮은 쪽에서 이동한다

    1)LEFT는 왼쪽 시작, RIGHT는 오른쪽 시작
    2)높이가 낮은 쪽에서 이동
    3)둘이 겹쳐지면 끝

    */
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int max = Integer.MIN_VALUE;
        while(left < right){
            int curValue = (right-left) * Math.min(height[left],height[right]);
            if(height[left]<=height[right]){
                left++;
                
            }else{
                right--;
            }
            
            if(max<curValue){
                max=curValue;
            }
        }
        return max;
    }
}