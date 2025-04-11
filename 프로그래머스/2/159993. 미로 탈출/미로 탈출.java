import java.util.*;
import java.io.*;

class Solution {
    static int startX = 0;
    static int startY = 0;
    
    static int leverX = 0;
    static int leverY = 0;
    
    static int n,m ;
    
    /*
    알고리즘 분류 : bfs
    어떻게 풀이? 
    시작 지점을 미리 찾아놓는다.
    1) 레버를 찾는다. 최소 횟수로 bfs
    2) 나간다. 최소 횟수로 bfs
    */
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        findPoint(maps);
        
        int lever = calLever(maps);
        int end = calEnd(maps);
        
        if(lever != -1 && end != -1){
            return lever+end;
        }
        else{
            return -1;
        }
    }
    static int calLever(String[] maps){
        int[] dx ={-1,1,0,0};
        int[] dy ={0,0,1,-1};
        
        boolean[][] visited = new boolean[n][m];
        visited[startX][startY] = true;
        
        Deque<int[]> queue = new ArrayDeque<>();
        queue.addFirst(new int[]{startX,startY,0});
        
        while(!queue.isEmpty()){
            int[] cur = queue.removeFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
        
        
        if (maps[x].charAt(y) == 'L'){
            leverX = x;
            leverY = y;
            return cnt;
        }
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (!visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny, cnt + 1});
                }
            }
        }
        
        
        }
        return -1;
    }
    
    static int calEnd(String[] maps){
        int[] dx ={-1,1,0,0};
        int[] dy ={0,0,1,-1};
        
        boolean[][] visited = new boolean[n][m];
        visited[leverX][leverY] = true;
        
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{leverX, leverY, 0});
        while(!queue.isEmpty()){
            int[] cur = queue.removeFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
            
            if (maps[x].charAt(y)=='E'){
                return cnt;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny, cnt + 1});
                    }
                }
            }
           
        }
        return -1;
    }
    
    
    
    static void findPoint(String[] maps){
        for(int i=0; i<maps.length; i++)
            for(int j=0; j<maps[0].length();j++){
                if(maps[i].charAt(j) =='S'){
                    startX = i;
                    startY = j;
                }
                else if (maps[i].charAt(j)==('L')){
                    leverX =i;
                    leverY =j;
                }
            }
        }
    
}
