import java.io.*;
import java.util.*;

public class Main {
    /*
    알고리즘 분류 : DFS
    어떻게 풀이
    DFS로 다 Visited에 추가하고, dfs 탐색 할 때마다 cnt+1
     */
    static int[][] map;
    static boolean[][] visited;
    static int m;
    static int n;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int gameCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < gameCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            int cabbageCount = Integer.parseInt(st.nextToken());

            map = new int[n][m];
            visited = new boolean[n][m];

            for (int k = 0; k < cabbageCount; k++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                map[b][a] = 1;
            }
//            System.out.println();
//            System.out.println("=== test case " + (i + 1) + " ===");
//            printMap(map);
            int bugCnt=0;
            for (int c = 0; c < m; c++) {
                for (int r = 0; r < n; r++) {
                    if (!visited[r][c] && map[r][c] == 1) {
                        visited[r][c] = true;
                        dfs(r, c);
                        bugCnt++;
                    }
                }
            }
            sb.append(bugCnt).append("\n");
        }
        System.out.print(sb.toString().trim());


    }
    static void dfs(int x, int y) {
        int[] dx = {0,1,-1,0};
        int[] dy = {1,0,0,-1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                if (map[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    dfs(nx,ny);
                }
            }

        }

    }
    static void printMap(int[][] map) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }
}