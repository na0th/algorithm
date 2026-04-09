import java.io.*;
import java.util.*;

public class Main {
    /*
    알고리즘 분류 : 다익스트라(가중치가 존재)
    어떻게 풀이 ?
    다익스트라
     */

    public static class Point{
        int x;
        int y;
        int cost;

        public Point(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int count = 0;
        while (true) {
            count++;
            int n = Integer.parseInt(br.readLine());
            int[][] map = new int[n][n];
            int[][] dist = new int[n][n];
            if (n == 0) {
                break;
            }
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for (int[] row : dist) {
                Arrays.fill(row, Integer.MAX_VALUE);
            }
            dist[0][0] = map[0][0];
            PriorityQueue<Point> pq = new PriorityQueue<>((o1,o2)-> o1.cost-o2.cost);
            pq.add(new Point(0, 0, map[0][0]));

            while (!pq.isEmpty()) {
                Point p = pq.poll();
                int x = p.x;
                int y = p.y;
                int cost = p.cost;
                // dist 보다 큰 경우는 무시합니다
                if(cost>dist[x][y]) continue;
                //마지막 지점에 도착하면 종료
                if(x == n-1 && y == n-1) break;

                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};

                for (int i = 0; i < 4; i++) {
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if (nx >= 0 && ny >= 0 && nx < n && ny < n) {
                        int newCost = cost + map[nx][ny];
                        if (newCost < dist[nx][ny]) {
                            dist[nx][ny] = newCost;
                            pq.add(new Point(nx,ny,newCost));
                        }
                    }
                }
            }
            sb.append("Problem ").append(count).append(": ").append(dist[n - 1][n - 1]).append("\n");
        }
        System.out.print(sb.toString().trim());
    }

//    private static void print() {
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                System.out.print(map[i][j] + " ");
//            }
//            System.out.println();
//        }
//    }
}