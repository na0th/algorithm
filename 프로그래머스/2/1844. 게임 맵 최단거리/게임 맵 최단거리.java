import java.util.*;
import java.io.*;
class Solution {
    /*
    최단 거리.. 동서남북 방향으로 한 칸씩 이동
    최단거리로 n,m에 도달했을 때의 최단거리 구하기
    
    알고리즘 분류 : BFS
    어떻게 풀이 ? 
    
    [i,j,cnt] 꼴로 정의해서 i,j까지 몇칸이라는 걸 의미하고
    그 상태에서 동서남북을 bfs 큐에 넣고 계속 pop해본다.
    n,m이 나왔을 때의 cnt를 출력하고, queue 다 끝났는데, 없었으면 -1 리턴
    
    추가 
    deque를 List<Integer> 가 아니고 int[]로 만든다. 
    deque.add(new int[] {} ) <= 이 꼴로 추가하면 됨.
    */
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
            
        Deque<int[]> deque = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,1,-1};
        
        int startX =0, startY =0; 

        visited[0][0]=true;
        deque.addLast(new int[]{startX,startY,1});
        
        while(!deque.isEmpty()){
            int[] pop = deque.removeFirst();
            int x = pop[0];
            int y = pop[1];
            int cnt = pop[2];
            if (x == n - 1 && y == m - 1) {
                return cnt;
            }
            
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx>=0 && nx < n && ny>=0 && ny < m){
                    if(maps[nx][ny] == 1 && !visited[nx][ny]){
                        visited[nx][ny] = true;
                        deque.addLast(new int[]{nx,ny,cnt+1});
                    }
                }
                
            
            }
        
        }
        return -1;
    }
}