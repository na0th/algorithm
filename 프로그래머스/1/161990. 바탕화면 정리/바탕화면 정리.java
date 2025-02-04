import java.util.*;
import java.io.*;
class Solution {
    /*
    왼쪽부터 제일 왼쪽이 어디인지? 제일 오른쪽이 어디인지?
    위아래로 제일 위가 어디인지? 제일 아래가 어디인지?
    
    왼쪽을 판단할 때는 처음 나오면 멈춤
    오른쪽을 판단할 때는 그냥 쭉 감
    위를 판단할 때는 처음 나오면 멈춤
    아래를 판단할 때는 그냥 쭉감
    
    알고리즘 분류 : 구현?
    */
    public int[] solution(String[] wallpaper) {
        int minRow = wallpaper.length, maxRow = -1;
        int minCol = wallpaper[0].length(), maxCol = -1;
        
        for(int i=0; i<wallpaper.length;i++){
            for(int j=0; j<wallpaper[i].length(); j++){
                if(wallpaper[i].charAt(j) == '#'){
                    minRow = Math.min(minRow, i);
                    maxRow = Math.max(maxRow,i);
                    minCol = Math.min(minCol,j);
                    maxCol = Math.max(maxCol,j);
                }
            }
        }
        int[] answer = {minRow, minCol, maxRow+1, maxCol+1 };
        return answer;
    }
}