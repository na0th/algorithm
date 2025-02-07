import java.util.*;
import java.io.*;
class Solution {
    /*
    상하좌우 갈 수 있으면 끝까지 간다.
    연결시켜서 최대 합을 더함..
    그 후 오름차순 정렬
    
    알고리즘 분류 : DFS? 영역 분리니까..
    어떻게 풀이? MAPS 전체를 돌면서 X가 아니면 visited에 있는지 체크하고 X아닌 걸 상하좌우 다 넣음..
    
    */
    
    
    public int[] solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        boolean[][] visited = new boolean[n][m];
        List<Integer> islandFoods = new ArrayList<>();
        
        
        
        
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(maps[i].charAt(j) != 'X' && !visited[i][j]){
                    int totalFood = dfs(maps,visited,i,j);
                    islandFoods.add(totalFood);
                }
            }
        }
        
        if (islandFoods.isEmpty()) {
            return new int[] {-1};
        }
        Collections.sort(islandFoods);
        
        int[] answer = new int[islandFoods.size()];
        for (int i = 0; i < islandFoods.size(); i++) {
            answer[i] = islandFoods.get(i);
        }
        return answer;
        
    }
    private int dfs(String[] maps, boolean[][] visited, int i, int j){
        int n = maps.length;
        int m = maps[0].length();
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        int cnt = 0;
        if (i>=0 && i< n && j>=0 && j < m  && !visited[i][j] && maps[i].charAt(j) != 'X'){
            visited[i][j] = true;
            
            cnt = maps[i].charAt(j) - '0';
            for(int k=0; k<4; k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                cnt+= dfs(maps,visited,nx,ny);
            }
        }
        return cnt;
        
        
    }
}