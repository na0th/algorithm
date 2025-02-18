import java.util.*;
import java.io.*;
class Solution {
    /**
    인접한 꽃이 없게 띄어서 꽃을 심을 수 있는지 여부

    알고리즘 분류 : 백트래킹? 완전탐색?
    어떻게 풀이? 
    앞쪽부터 심는다.
    심기 전에 왼쪽,오른쪽에 꽃이 있는지 확인하고 없으면 심는다.
    꽃을 심을 수 없는 경우 종료한다
    -> 꽃이 남았다면 false, 0개면 true
     */
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        for(int i=0; i<flowerbed.length; i++){
            if(i == 0){
                if(flowerbed[i] == 0 && (flowerbed.length == 1 || flowerbed[i + 1] == 0)){
                    flowerbed[i]=1;
                    n--;
                }
            }    
            else if(i == flowerbed.length-1){
               if(flowerbed[i]==0 && flowerbed[i-1]== 0){
                    flowerbed[i]=1;
                    n--;
                }
            }
            else{
                if(flowerbed[i]==0 &&flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    flowerbed[i]=1;
                    n--;
                }
                
            }
            if(n==0) return true;
        }
        return n<=0;
    }
}