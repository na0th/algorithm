import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static class Point{
        int x;
        int t;
        Point(int x, int t) {
            this.x = x;
            this.t = t;
        }
    }
    public static void main(String[] args) throws IOException {
        /*
        수빈이는 숨바꼭질을 하고 있다.
        수빈이는 0<= n <= 100000, 동생은 0<=k<=100000 이고
        수빈이는 1. 걷기 2. 순간이동
        걷기는 위치가 X일 때, 1초 후에 X-1, X+1 이동
        순간이동은 위치가 X일 때, 1초 후에 2X로 이동
        수빈이와 동생의 위치가 주어졌을 떄,수빈이가 동생을 가장 빨리 찾는 시간을 구하기

        알고리즘 분류 : BFS
        어떻게 풀이?
        1. 해당 위치, 해당 시간은 (X,T) -> (X-1, T+1) , (X+1, T+1) , (2X, T+1)이 생김
        2. 수빈이의 위치 X가 동생의 위치를 넘은 경우는 PASS, 못 넘은 경우는 또 3가지 추가
        3. 같은 경우는 끝낸다

        아마 방문한 경우는 넘어가는 최적화가 필요할 듯싶다.

        * */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        Deque<Point> queue = new ArrayDeque<>();

        String[] parts = br.readLine().split(" ");
        int start = Integer.parseInt(parts[0]);
        int end = Integer.parseInt(parts[1]);

        queue.add(new Point(start,0));
        boolean[] visited = new boolean[100001];

        sb.append(find(queue, visited, end));
        System.out.print(sb.toString().trim());
    }

    public static int find(Deque<Point> queue, boolean[] visited, int end) {
        while (!queue.isEmpty()) {
            Point p = queue.removeFirst();

            int x = p.x;
            int t = p.t;

            if (x == end) return t;
            int[] next = {2 * x, x + 1, x - 1};
            for (int nx : next) {
                if (nx >= 0 && nx <= 100000 && !visited[nx]) {
                    visited[nx] = true;
                    queue.add(new Point(nx, t + 1));
                }
            }
        }
        return -1;
    }
}
