import java.util.*;
import java.io.*;

class Solution {
    static int startX = 0;
    static int startY = 0;
    
    static int leverX = 0;
    static int leverY = 0;
    /*
    알고리즘 분류 : bfs
    어떻게 풀이? 
    시작 지점을 미리 찾아놓는다.
    1) 레버를 찾는다. 최소 횟수로 bfs
    2) 나간다. 최소 횟수로 bfs
    */
    public int solution(String[] maps) {
        
        findPoint(maps);
        
        if(calLever(maps) ==-1 || calEnd(maps) == -1){
            return -1;
        }
        return calLever(maps)+calEnd(maps);
        
    
    }
    static int calLever(String[] maps){
        int[] dx ={-1,1,0,0};
        int[] dy ={0,0,1,-1};
        
        Set<List<Integer>> visited = new HashSet<>();
        visited.add(Arrays.asList(startX,startY));
        
        Deque<List<Integer>> queue = new ArrayDeque<>();
        queue.add(Arrays.asList(startX,startY,0));
        
        while(!queue.isEmpty()){
            List<Integer> pop = queue.removeFirst();
            int x = pop.get(0);
            int y = pop.get(1);
            int cnt = pop.get(2);
            
            if(maps[x].charAt(y)=='L'){
                return cnt;
            }
            for(int i=0; i<dx.length; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if( (0<= nx &&  nx <maps.length ) && (0<=ny && ny<maps[nx].length()) ){
                    if(!visited.contains(Arrays.asList(nx,ny)) && maps[nx].charAt(ny)!='X'){
                        visited.add(Arrays.asList(nx,ny));
                        queue.add(Arrays.asList(nx,ny,cnt+1));
                    }
                    
                }
            }    
        }
        return -1;
    }
    
    static int calEnd(String[] maps){
        int[] dx ={-1,1,0,0};
        int[] dy ={0,0,1,-1};
        
        Set<List<Integer>> visited = new HashSet<>();
        visited.add(Arrays.asList(leverX,leverY));
        
        Deque<List<Integer>> queue = new ArrayDeque<>();
        queue.add(Arrays.asList(leverX,leverY,0));
        
        while(!queue.isEmpty()){
            List<Integer> pop = queue.removeFirst();
            int x = pop.get(0);
            int y = pop.get(1);
            int cnt = pop.get(2);
            
            if (maps[x].charAt(y)=='E'){
                return cnt;
            }
            
            for(int i=0; i<dx.length; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if( (0<= nx &&  nx <maps.length ) && (0<=ny && ny<maps[nx].length()) ){
                    if(!visited.contains(Arrays.asList(nx,ny)) && maps[nx].charAt(ny)!='X'){
                        visited.add(Arrays.asList(nx,ny));
                        queue.add(Arrays.asList(nx,ny,cnt+1));
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
