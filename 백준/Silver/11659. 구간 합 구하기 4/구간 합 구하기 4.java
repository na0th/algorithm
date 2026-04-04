import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
   /*
   수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
    5 3
    5 4 3 2 1
    1 3
    2 4
    5 5
    알고리즘 분류 : 배열? dp?
    어떻게 풀이
    1. 순회하면서 해당 순서까지 합을 구한다.
    2. 1~3은 dist[3]-dist[0]  = 1 2 3 - 0
       2~4는 dist[4]-dist[1] =  1 2 3 4 - 1 = 9
   * */
    static int[] dist;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        dist = new int[n+1];
        int accDist = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            int curDist = Integer.parseInt(st.nextToken());
            accDist += curDist;
            dist[i] = accDist;
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            sb.append(func(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            sb.append("\n");
        }
        System.out.print(sb.toString().trim());
    }

    public static int func(int start, int end) {
        return dist[end] - dist[start-1];
    }
}
