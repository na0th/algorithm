import java.io.*;
import java.util.*;

public class Main {
    /*
    토마토가 익는 최소 일자 구하기.
    토마토가 익었다 1
    토마토가 익지 않았다 0
    토마토가 들어있지 않은 칸 -1
    알고리즘 분류 : BFS(최소 COST?)
    어떻게 풀이
    토마토 좌표를 큐에 추가한다.
    큐에서 토마토 뽑고, 가능한 경로 다 큐에 추가(이동할 떄 마다 day +1)
    뽑을 때마다, 목표한 토마토 갯수가 됐는지 확인. -> 큐 끝날 떄까지 안되면 -1리턴

    6 4
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 1
     */
    public static class Point {
        int x;
        int y;
        int day;
        public Point(int x, int y, int day) {
            this.x = x;
            this.y = y;
            this.day = day;
        }
    }
    static int[][] map;
    static boolean[][] visited;
    static int col;
    static int row;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        col = Integer.parseInt(st.nextToken());
        row = Integer.parseInt(st.nextToken());
        map = new int[row][col];
        visited = new boolean[row][col];
        ArrayDeque<Point> queue = new ArrayDeque<>();
        for (int i = 0; i < row; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < col; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                //익은 토마토를 큐에 추가
                if(map[i][j] == 1){
                    queue.addFirst(new Point(i, j, 0));
                    visited[i][j] = true;
                }

            }
        }
        // 갈 수 없는 곳 빼고는 다 토마토가 되어야 한다(종료 조건)
        int wallCount = count(-1);
//        printMap();

        int lastDay = 0;
        while (!queue.isEmpty()) {
            Point p = queue.pollLast();
            int x = p.x;
            int y = p.y;
            int day = p.day;
            //큐 밖에서도 쓰려고
            lastDay = p.day;

            int[] dx = {0,0,1,-1};
            int[] dy = {-1,1,0,0};

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < row && ny < col) {
                    if (map[nx][ny] == 0 && !visited[nx][ny]) {
                        queue.addFirst(new Point(nx, ny, day + 1));
                        map[nx][ny]=1;
                        visited[nx][ny]=true;
                    }
                }
            }
        }
        // 종료 조건
        // if 익은 토마토 갯수가 초기 토마토 갯수 + 0의 갯수가 아니면 return -1 맞으면 return day
        int rTomatoCnt = count(1);
        if (rTomatoCnt == row * col - wallCount) {
            System.out.print(lastDay);
        }else{
            System.out.print(-1);
        }





    }

    private static int count(int x) {
        int cnt = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (map[i][j] == x) cnt++;
            }
        }
        return cnt;
    }

    public static void printMap() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }
}