import java.util.*;
class Solution {
    /*
    모든 명함을 수납할 수 있는 가장 작은 지갑을 만들기
    [[60, 50], [30, 70], [60, 30], [80, 40]]
    분류 : 완전탐색(최댓값 구하기)
    어떻게 풀이? 
    1. 가로, 세로중 더 큰 길이를 가로에 두게 정렬한다.
    2. for문 순회하면서 w의 최댓값, h의 최댓값을 구한다.
    3. max_w, max_h를 곱한다
    */
    public int solution(int[][] sizes) {
        int answer = 0;
        int max_w = 0 , max_h = 0;
        for(int[] wh : sizes){
            if(wh[0]<wh[1]){
                int temp = wh[0];
                wh[0] = wh[1];
                wh[1] = temp;                
            }
            if(max_w < wh[0]){
                max_w = wh[0];
            }
            if(max_h < wh[1]){
                max_h = wh[1];
            }
        }
        return max_w * max_h;
    }
}