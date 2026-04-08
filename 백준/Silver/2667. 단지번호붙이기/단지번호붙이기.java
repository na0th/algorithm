import java.io.*;
import java.util.*;

public class Main {
    /*
    집 영역끼리 구분한다.
     알고리즘 분류 : DFS
     어떻게 풀이?
    1. 전체 2중 FOR문 순회하면서, 집이 나오면 동서남북 연결
    2. 2중 FOR문 순회하면서 집 영역의 갯수 COUNT한 후 출력
     */
    static int n;
    static int[][] map;
    static boolean[][] visited;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }
//        printMap(n, map);
        int areaCount = 0;
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    visited[i][j] = true;
                    answer.add(dfs(i, j, 1));
                    areaCount++;
                }
            }
        }
        Collections.sort(answer);
        StringBuilder sb = new StringBuilder();

        sb.append(areaCount).append("\n");
        for (int areaSum : answer) {
            sb.append(areaSum).append("\n");
        }
        System.out.print(sb.toString().trim());

    }

    private static int dfs(int x, int y, int count) {
        visited[x][y] = true;

        int[] dx = {-1,1,0,0};
        int[] dy = {0, 0, 1, -1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                if(map[nx][ny] == 1 && !visited[nx][ny]){
                    count = dfs(nx,ny,count+1);
                }
            }
        }
        return count;
    }

    private static void printMap(int n, int[][] map) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(map[i][j] +" ");
            }
            System.out.println();
        }
    }
}